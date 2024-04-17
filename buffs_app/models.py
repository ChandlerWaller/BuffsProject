from django.db import models
from django.urls import reverse
from django.views import generic

# Create your models here.

class Shift(models.Model):

    #List of choices for shift position
    POSITION = (
    ('1st Bar', 'First Person Cut in Bar'),
    ('1st Dinning', 'First Person Cut in Dinning'),
    ('Late Stay Bar', 'Second Person Cut in Bar'),
    ('Late Stay Dinning', 'Second Person Cut in Dinning'),
    ('Carpet Closer', 'Closer for Dinning'),
    ('Bar Closer', 'Closer for Bar')
    )
    date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    time = models.TimeField(blank=False)
    is_available = models.BooleanField(default=True)
    position = models.CharField(max_length=200, choices=POSITION, default='Position of Shift')
    username = models.CharField(max_length=200, default=" ")
    def __str__(self):
        return (self.position + " " + str(self.date) + " " + self.username)
    def get_absolute_url(self):
        return reverse('shift-detail', args=[str(self.id)])

class ShiftListView(generic.ListView):
    model = Shift

class ShiftDetailView(generic.DetailView):
    model = Shift
    