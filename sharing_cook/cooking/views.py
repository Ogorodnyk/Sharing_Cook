from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from cooking.models import Users, Cuisine
from datetime import datetime

def index(request):
    return render(request, "index.html",)

def cuisine(request):
    cuisines = Cuisine.objects.all()
    return render(request, "cuisine.html",context={"cuisines": cuisines,})

def waste_food(request):
    return render(request, "waste_food.html",)

def meet(request):
    users = Users.objects.all()
    count = Users.objects.count()
    #birthday = int((datetime.now().date() - Users.birth_date).days / 365.25)
    #return render(request,  "meet.html", context={"users": users,"count": count,"birthday": birthday,},)
    return render(request,  "meet.html", context={"users": users,"count": count,},)


def user(request,pk):
    user = Users.objects.get(pk=pk)
    return render(request,"user.html", context={"user": user,})

def message(request):
    return render(request, "message.html",)

def pay(request):
    return render(request, "pay.html",)

def rezervation(request):
    return render(request, "rezervation.html",)

def experience(request):
    return render(request, "experience.html",)

def contact(request):
    return render(request, "contact.html",)





