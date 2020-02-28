from django.contrib import admin

# Register your models here.
from cooking.models import CustomUser, Cuisine, Message,Event
admin.site.register(CustomUser)
admin.site.register(Cuisine)
admin.site.register(Message)
admin.site.register(Event)


