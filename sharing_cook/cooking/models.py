from django.db import models
from django.conf import settings


from django.utils import timezone
from datetime import datetime, timezone
from django.contrib.auth.models import User, UserManager
from django_countries.fields import CountryField
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')



# from django.contrib.auth import get_user_model


# Create your models here.
class CustomUser(User):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    birth_date = models.DateField(blank=True, null=True)
    language_1 = models.CharField(max_length=32)
    language_2 = models.CharField(max_length=32, blank=True, null=True)
    language_3 = models.CharField(max_length=32, blank=True, null=True)
    country = CountryField(default='')

    @property
    def age(self):
        age = int(
            (datetime.now().date() - self.birth_date).days / 365.25)  ### help count how old users, no needed do migrate
        return (f"{age} year old")


class Cuisine(models.Model):
    name = models.CharField(max_length=48)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name






class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender",on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver",on_delete=models.CASCADE)
    msg_content = models.CharField(max_length=256)
    date = models.DateField(default=datetime.now)

# class MessageManager(models.Manager):
#
#     def msg_content(self, receiver):
#         """
#         Returns all messages that were received by the given user and are not
#         marked as deleted.
#         """
#         return self.filter(
#             receiver=receiver,
#             receiver_deleted_at__isnull=True,
#         )


class Event(models.Model):

    COST_CHOISES = (
        ('M', 'Money'),
        ('P', 'Product'),
        ('C', "Help with cooking"),
        ('D', "Help with wash dish"),
    )

    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    people = models.IntegerField()
    date = models.DateTimeField()
    place = models.CharField(max_length=128)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    meal = models.CharField(max_length=256,default='')
    cost = models.CharField(max_length=1, choices=COST_CHOISES, default='M')

    def __str__(self):
        return f"{self.owner} create event to {self.people} people cuisine {self.cuisine}"