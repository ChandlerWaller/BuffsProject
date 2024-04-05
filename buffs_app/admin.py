from django.contrib import admin

# Register your models here.

from .models import Shift, Server # to add a new model use a comma here

admin.site.register(Server) #repeat this line for each new model
admin.site.register(Shift)