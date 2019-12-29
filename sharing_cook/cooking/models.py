from django.db import models
from datetime import datetime

# Create your models here.
class Users(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    birth_date = models.DateField(blank=True, null=True)
    languages = models.CharField(max_length=32)

    @property
    def age(self):
        return int((datetime.now().date() - self.birth_date).days / 365.25)  ### help count how old users, no needed do migrate

class Cuisine(models.Model):
    name = models.CharField(max_length=48)
