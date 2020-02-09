"""sharing_cook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from cooking.views import *
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(), name="index"),
    path('meet/',MeetView.as_view(), name="meet"),
    path('cuisine/', CuisineView.as_view(), name='cuisine'),
    path('waste_food/', WasteFoodView.as_view(), name='waste_food'),
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('user_list/', UserListView.as_view(), name='user-list'),
    path('add_user/', AddUserView.as_view(), name='add_user'),
    path('pay/', pay),
    path('rezervation/', rezervation),
    path('message/', message),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    path('user_detail/<int:custom>/', UserrView.as_view(), name="user"),

]
