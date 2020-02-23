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
from django.urls import path, include
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
    path('user_detail/<int:custom>/', UserView.as_view(), name="user"),
    path('message_detail/<int:message>/', MessageView.as_view(), name="message"),
    url(regex=r"^friends/(?P<username>[\w-]+)/$", view=view_friends, name="friendship_view_friends",),
    url(r'^friendship/', include('friendship.urls')),
    path('show_friends/', ShowFriendView.as_view(), name="show_friends"),
    path('inbox/', InboxView.as_view(), name="inbox"),
    path('outbox/', OutBoxView.as_view(), name="outbox"),
    path('show_request/', ShowRequestView.as_view(), name="show_request"),
    url(regex=r"^friend/add/(?P<to_username>[\w-]+)/$", view=friendship_add_friend, name="friendship_add_friend",),
    url(
        regex=r"^friend/reject/(?P<friendship_request_id>\d+)/$",
        view=friendship_reject,
        name="friendship_reject",
    ),
    url(
        regex=r"^friend/requests/rejected/$",
        view=friendship_request_list_rejected,
        name="friendship_requests_rejected",
    ),
    url(r'^send_message/',  MessagesSendView.as_view(),
        name="message_create"),

    # path(r'inbox/', inbox, name='messages_inbox'),
]