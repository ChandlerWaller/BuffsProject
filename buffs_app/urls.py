from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('logout', views.logout_view, name='logout'),
path('login', views.login_view, name='login'),
path('shifts/', views.ShiftListView.as_view(), name= 'shifts'),
path('shift/<int:pk>', views.ShiftDetailView.as_view(), name='shift-detail'),
path('update_shift/<int:pk>', views.updateShift, name='update-shift'),
path('create_shift', views.createShift, name='create-shift'),
path('delete_shift/<int:pk>', views.deleteShift, name='delete-shift'),
]
