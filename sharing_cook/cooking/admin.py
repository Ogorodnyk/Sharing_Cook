from django.contrib import admin

# Register your models here.
from cooking.models import Users, Cuisine
admin.site.register(Users)
admin.site.register(Cuisine)

