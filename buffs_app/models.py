from django.db import models
from django.urls import reverse
from django.views import generic

# Create your models here.

class Server(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
#Returns the URL to access a particular instance of MyModelName.
#if you define this method then Django will automatically
# add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('server-detail', args=[str(self.id)])


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
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    position = models.CharField(max_length=200, choices=POSITION, default='Position of Shift')
    def __str__(self):
        return (self.position + " " + str(self.date) + " " + self.server.name)
    def get_absolute_url(self):
        return reverse('shift-detail', args=[str(self.id)])

class ServerDetailView(generic.DetailView):
    model = Server

class ShiftListView(generic.ListView):
    model = Shift

class ShiftDetailView(generic.DetailView):
    model = Shift
    