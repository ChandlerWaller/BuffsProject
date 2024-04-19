from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields =('date', 'time', 'is_available', 'position',)

class LoginForm(ModelForm):
    class Meta:
        model = UserModel
        fields =('Username', 'Password')

class TakenShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields =('Taken_By',)