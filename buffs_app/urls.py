from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('logout', views.logout, name='logout'),
path('login', views.login, name='login'),
path('shifts/', views.ShiftListView.as_view(), name= 'shifts'),
path('server/<int:pk>', views.server_detail , name='server-detail'),
path('shift/<int:pk>', views.ShiftDetailView.as_view(), name='shift-detail'),
path('server/<int:server_id>/update_shift/<int:pk>', views.updateShift, name='update-shift'),
path('server/<int:server_id>/create_shift', views.createShift, name='create-shift'),
path('server/<int:server_id>/delete_shift/<int:pk>', views.deleteShift, name='delete-shift'),
path('server/<int:server_id>', views.updateServer, name='update-server'),
]
