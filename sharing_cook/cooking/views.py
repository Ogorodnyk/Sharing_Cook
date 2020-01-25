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


# class SchoolView(View):
#     def get(self, request):
#         ctx = {
#             'class_list': SCHOOL_CLASS
#         }
#         return render(request, 'school.html', ctx)


class IndexView(View):
    def get(self, request):
        return render(request, "index.html", )


def cuisine(request):
    cuisines = Cuisine.objects.all()
    return render(request, "cuisine.html", context={"cuisines": cuisines, })


def waste_food(request):
    return render(request, "waste_food.html", )


def meet(request):
    users = CustomUser.objects.all()
    count = CustomUser.objects.count()
    return render(request, "meet.html", context={"users": users, "count": count, }, )


def user(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, "user.html", context={"user": user, })


def message(request):
    return render(request, "message.html", )


def pay(request):
    return render(request, "pay.html", )


def rezervation(request):
    return render(request, "rezervation.html", )


def experience(request):
    return render(request, "experience.html", )


def contact(request):
    return render(request, "contact.html", )


class UserListView(View):

    def get(self, request):
        customs = CustomUser.objects.all()
        return render(request, 'user_list.html', {'customs': customs,})


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
            try:
                User.objects.create_user(password=new_password, username=new_login, first_name=new_first_name,
                                         last_name=new_last_name, email=new_email)
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
