from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.models import User
from .models import Message, Cuisine, Event

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

COST_CHOISES = (
    ('M', 'Money'),
    ('P', 'Product'),
    ('C', "Help with cooking"),
    ('D', "Help with wash dish"),
)

class AddUserForm(forms.Form):
    login = forms.CharField(max_length=64, label="Login")
    password = forms.CharField(max_length=64, widget=forms.PasswordInput, label="Password")
    password_repeat = forms.CharField(max_length=64, widget=forms.PasswordInput, label="Repeat password")
    first_name = forms.CharField(max_length=64, label="Name")
    last_name = forms.CharField(max_length=64, label="Last Name")
    email = forms.EmailField(max_length=128, label="Email")
    gender = forms.ChoiceField(label="Gender M/F", choices=GENDER_CHOICES)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2010)), label="Birth_date YY-MM-DD")
    language_1 = forms.CharField(max_length=32, label="Language_1", required=False)
    language_2 = forms.CharField(max_length=32, label="Languages_2", required=False)
    language_3 = forms.CharField(max_length=32, label="Languages_3", required=False)
    country = CountryField().formfield()

    def clean_password_repeat(self):
        password = self.cleaned_data.get("password")
        password_repeat = self.cleaned_data.get("password_repeat")
        if password and password_repeat and password != password_repeat:
            raise forms.ValidationError("Passwords no match")
        return password_repeat


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['Password no match'],
                code='password_mismatch',
            )
        return password2


class RelationshipForm(forms.Form):
    from_person = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    to_person = forms.ModelChoiceField(queryset=User.objects.all(), required=True)


class MessageForm(forms.Form):
    # sender = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    receiver = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    msg_content = forms.CharField(widget=forms.Textarea())


    def save(self, sender, ):
        receiver = self.cleaned_data['receiver']
        msg_content = self.cleaned_data['msg_content']
        message_list = []

        # for r in receiver:
        msg = Message(
            sender = sender,
                receiver = receiver,
             msg_content = msg_content,
        )
        msg.save()
        message_list.append(msg)

        return message_list

class MessageDirectForm(forms.Form):
    msg_content = forms.CharField(widget=forms.Textarea())

    def save(self, sender, receiver ):
        # receiver = self.cleaned_data['receiver']
        msg_content = self.cleaned_data['msg_content']

        message_list = []

        # for r in receiver:
        msg = Message(
            sender = sender,
            receiver = receiver,
             msg_content = msg_content,
        )
        msg.save()
        message_list.append(msg)

        return message_list



class EventCreateForm(forms.Form):
    # sender = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    people = forms.IntegerField()
    date = forms.DateTimeField(widget=forms.SelectDateWidget())
    time = forms.TimeField(widget=forms.TimeInput())
    place = forms.CharField()
    cuisine = forms.ModelChoiceField(queryset=Cuisine.objects.all(), required=True)
    meal = forms.CharField(widget=forms.Textarea())
    cost = forms.ChoiceField(label="COST", choices=COST_CHOISES)


    def save(self, owner, ):
        people = self.cleaned_data['people']
        date = self.cleaned_data['date']
        time = self.cleaned_data['time']
        place = self.cleaned_data['place']
        cuisine = self.cleaned_data['cuisine']
        meal = self.cleaned_data['meal']
        cost = self.cleaned_data['cost']
        event_list = []

        # for r in receiver:
        event = Event(
            owner = owner,
            people = people,
             date = date,
            place= place,
            cuisine = cuisine,
        meal = meal,
            cost=cost
        )
        event.save()
        event_list.append(event)

        return event_list