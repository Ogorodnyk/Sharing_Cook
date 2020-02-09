from django.db import models
from django.utils import timezone
from datetime import datetime, timezone
from django.contrib.auth.models import User, UserManager
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model


# Create your models here.
class CustomUser(User):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    birth_date = models.DateField(blank=True, null=True)
    language_1 = models.CharField(max_length=32, default='')
    language_2 = models.CharField(max_length=32, default='')
    language_3 = models.CharField(max_length=32, default='')
    country = CountryField(default='')

    @property
    def age(self):
        age = int(
            (datetime.now().date() - self.birth_date).days / 365.25)  ### help count how old users, no needed do migrate
        return (f"{age} year old")


class Cuisine(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name
