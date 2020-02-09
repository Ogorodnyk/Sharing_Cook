from sqlite3 import IntegrityError

from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from cooking.models import CustomUser, Cuisine
from datetime import datetime
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import AddUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView


class IndexView(View):
    def get(self, request):
        return render(request, "index.html", )


class MeetView(View):
    def get(self, request, ):
        users = CustomUser.objects.all()
        count = CustomUser.objects.count()
        ctx = {
            'users': users,
            "count": count,
        }
        return render(request, 'meet.html', ctx)


class CuisineView(View):
    def get(self, request):
        cuisines = Cuisine.objects.all()
        ctx = {
            'cuisines': cuisines,
        }
        return render(request, "cuisine.html", ctx)


class WasteFoodView(View):
    def get(self, request):
        return render(request, "waste_food.html", )


class ExperienceView(View):
    def get(self, request):
        return render(request, "experience.html", )


class ContactView(View):
    def get(self, request):
        return render(request, "contact.html", )


class UserrView(View):
    def get(self, request, custom):
        custom = CustomUser.objects.get(pk=custom)
        ctx = {
            'custom': custom,

        }
        return render(request, 'user.html', ctx)


def message(request):
    return render(request, "message.html", )


def pay(request):
    return render(request, "pay.html", )


def rezervation(request):
    return render(request, "rezervation.html", )


class UserListView(View):

    def get(self, request):
        customs = CustomUser.objects.all()
        return render(request, 'user_list.html', {'customs': customs, })


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'add_user.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            new_login = form.cleaned_data['login']
            new_password = form.cleaned_data['password']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            birth_date = form.cleaned_data['birth_date']
            language_1 = form.cleaned_data['language_1']
            language_2 = form.cleaned_data['language_2']
            language_3 = form.cleaned_data['language_3']
            country = form.cleaned_data['country']
            try:
                CustomUser.objects.create_user(password=new_password, username=new_login, first_name=new_first_name,
                                               last_name=new_last_name, email=new_email, gender=gender,
                                               birth_date=birth_date,
                                               language_1=language_1, language_2=language_2,
                                               language_3=language_3, country=country)
            except IntegrityError:
                response = "Login is busy, please give another login"
                return render(request, 'add_user.html', {'form': form,
                                                         'response': response})
            return render(request, 'successful_registered.html')
        return render(request, 'add_user.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse(f"Hello {user}")
                    return redirect(reverse_lazy('index'))
                else:
                    return HttpResponse('')
            else:
                return HttpResponse('Uncorrected password')
    else:
        form = LoginForm()
    return render(request, 'log_in.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('index'))


class UserView(View):
    def get(self, request, ):
        if request.user.has_perm('advanced_django.add_product'):
            users = CustomUser.objects.all()
            ctx = {
                'users': users,
            }
        return render(request, 'products.html', ctx)
