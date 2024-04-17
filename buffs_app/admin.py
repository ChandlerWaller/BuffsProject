from django.contrib import admin

# Register your models here.

from .models import Shift # to add a new model use a comma here

#repeat this line for each new model
admin.site.register(Shift)