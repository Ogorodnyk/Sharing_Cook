# Create your views here.
from sqlite3 import IntegrityError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cooking.models import CustomUser, Cuisine, Message, Event
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import AddUserForm, LoginForm, MessageForm, MessageDirectForm, EventCreateForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
from django.shortcuts import get_object_or_404
from django.conf import settings
from friendship.models import Friend, Follow, FriendshipRequest, Block
from django.contrib import messages

try:
    from django.contrib.auth import get_user_model

    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

    user_model = User

get_friendship_context_object_name = lambda: getattr(
    settings, "FRIENDSHIP_CONTEXT_OBJECT_NAME", "user"
)
get_friendship_context_object_list_name = lambda: getattr(
    settings, "FRIENDSHIP_CONTEXT_OBJECT_LIST_NAME", "users"
)

from friendship.exceptions import AlreadyExistsError


class IndexView(View):
    def get(self, request):
        return render(request, "index.html", )


class MeetView(View):
    def get(self, request):
        users = CustomUser.objects.all()
        count = CustomUser.objects.count()
        ctx = {
            'users': users,
            "count": count,
        }
        return render(request, 'meet.html', ctx)


def view_friends(request, username, template_name="friendship/friend/user_list.html"):
    """ View the friends of a user """
    user = get_object_or_404(user_model, username=username)
    friends = Friend.objects.friends(request.user)
    return render(request, template_name, {
        get_friendship_context_object_name(): user,
        'friendship_context_object_name': get_friendship_context_object_name(),
        'friends': friends,
    })


class ShowFriendView(View):
    def get(self, request):
        if request.user.is_authenticated:
            friends = Friend.objects.friends(request.user)
            return render(request, "show_friends.html", {'friends': friends}, )


class ShowRequestView(View):
    def get(self, request):
        if request.user.is_authenticated:
            requests = Friend.objects.unread_requests(user=request.user)
            return render(request, "show_request.html", {"requests": requests}, )


@login_required
def friendship_requests_detail(
        request, friendship_request_id, template_name="friendship/friend/request.html"
):
    """ View a particular friendship request """
    f_request = get_object_or_404(FriendshipRequest, id=friendship_request_id)

    return render(request, template_name, {"friendship_request": f_request})


class CuisineView(View):
    def get(self, request):
        cuisines = Cuisine.objects.all()
        ctx = {
            'cuisines': cuisines,
        }
        return render(request, "cuisine.html", ctx)

class CuisineDetailView(View):
    def get(self, request, cuisine):
        cuisine = Cuisine.objects.get(pk=cuisine)
        ctx = {
            'cuisine': cuisine,
        }
        return render(request, "show_cuisine.html", ctx)


class WasteFoodView(View):
    def get(self, request):
        return render(request, "waste_food.html", )



class ContactView(View):
    def get(self, request):
        return render(request, "contact.html", )


class UserView(View):
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


class AddFriendRequestView(View):
    def post(self, request, to_user):
        to_user = user_model.objects.get(username=to_user)
        Friend.objects.add_friend(
            request.user,  # The sender
            to_user,  # The recipient
            message='Hi! I would like to add you')  # This message is optional

        return redirect(reverse_lazy('user'))


class AddFriendRequestView(View):
    def post(self, request, to_user):
        to_user = user_model.objects.get(username=to_user)
        Friend.objects.add_friend(
            request.user,  # The sender
            to_user,  # The recipient
            message='Hi! I would like to add you')  # This message is optional

        return redirect(reverse_lazy('user'))


@login_required
def friendship_add_friend(
        request, to_username, template_name="friendship/friend/add.html"
):
    """ Create a FriendshipRequest """
    ctx = {"to_username": to_username}

    if request.method == "POST":
        to_user = CustomUser.objects.get(username=to_username)
        from_user = request.user
        try:
            Friend.objects.add_friend(from_user, to_user, message='Hi! I would like to add you to Friend')
        except AlreadyExistsError as e:
            ctx["errors"] = ["%s" % e]
        else:
            return redirect("show_friends")

    return render(request, template_name, ctx)


@login_required
def friendship_reject(request, friendship_request_id):
    """ Reject a friendship request """
    if request.method == "POST":
        f_request = get_object_or_404(
            request.user.friendship_requests_received, id=friendship_request_id
        )
        f_request.reject()
        return redirect("friendship_request_list")

    return redirect(
        "friendship_requests_detail", friendship_request_id=friendship_request_id
    )


@login_required
def friendship_request_list_rejected(
        request, template_name="friendship/friend/requests_list.html"
):
    """ View rejected friendship requests """
    # friendship_requests = Friend.objects.rejected_requests(request.user)
    friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=False)

    return render(request, template_name, {"requests": friendship_requests})


class MessagesSendView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = MessageForm()
            return render(request, 'send_messages.html', {'form': form})

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save(sender=request.user)
        return redirect(reverse_lazy('outbox'))


class MessagesDirectView(View):
    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            form = MessageDirectForm()
            return render(request, 'send_messages.html', {'form': form})

    def post(self, request, receiver):
        form = MessageDirectForm(request.POST)
        if form.is_valid():
            receiver = CustomUser.objects.get(pk=receiver)  # Wybieramy usera na ktorego weszlismy
            form.save(sender=request.user, receiver=receiver)
            return redirect(reverse_lazy('outbox'))


class InboxView(View):
    def get(self, request):
        if request.user.is_authenticated:
            message_list = Message.objects.filter(receiver=request.user.id)
            return render(request, "show_message.html", {'message_list': message_list}, )


class OutBoxView(View):
    def get(self, request):
        if request.user.is_authenticated:
            message_list = Message.objects.filter(sender=request.user.id)
            return render(request, "show_message_outbox.html", {'message_list': message_list}, )


class MessageView(View):
    def get(self, request, message):
        message = Message.objects.get(pk=message)
        ctx = {
            'message': message,

        }
        return render(request, 'message_view.html', ctx)


class EventCreate(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = EventCreateForm()
            return render(request, 'event_create.html', {'form': form})

    def post(self, request):
        form = EventCreateForm(request.POST)
        if form.is_valid():
            form.save(owner=request.user)
        return redirect(reverse_lazy('my_event'))

class MyEventView(View):
    def get(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            event_list = Event.objects.filter(owner=request.user)
            return render(request, "show_event.html", {'event_list': event_list}, )

class AllEventView(View):
    def get(self, request):
        events = Event.objects.all()
        ctx = {
            'events': events,
        }
        return render(request, "all_event.html", ctx)

class EventView(View):
    def get(self, request, event):
        event = Event.objects.get(pk=event)
        ctx = {
            'event': event,

        }
        return render(request, 'event.html', ctx)

class EventUserView(View):
    def get(self, request, events_user):
        events_user = Event.objects.filter(owner=events_user)
        ctx = {
            'events_user': events_user,

        }
        return render(request, 'show_event_user.html', ctx)