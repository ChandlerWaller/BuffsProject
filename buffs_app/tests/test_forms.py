from django.test import TestCase
from django.utils import timezone

from buffs_app.forms import *

class ShiftFormTest(TestCase):
    def test_date(self):
        form = ShiftForm()
        self.assertTrue(form.fields['date'].label is None or form.fields['date'].label == 'Date')

    def test_time(self):
        form = ShiftForm()
        self.assertTrue(form.fields['time'].label is None or form.fields['time'].label == 'Time')

class LoginFormTest(TestCase):
    def test_username(self):
        form = LoginForm()
        self.assertTrue(form.fields['Username'].label is None or form.fields['Username'].label == 'Username')

    def test_password(self):
        form = LoginForm()
        self.assertTrue(form.fields['Password'].label is None or form.fields['Password'].label == 'Password')