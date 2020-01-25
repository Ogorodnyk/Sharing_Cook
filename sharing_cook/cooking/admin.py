from django.contrib import admin

# Register your models here.
from cooking.models import CustomUser, Cuisine
admin.site.register(CustomUser)
admin.site.register(Cuisine)

