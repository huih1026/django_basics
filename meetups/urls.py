from django.urls import path
from . import views

urlpatterns = [
    path('', views.meetups, name='meetups'),
    path('register/<slug:slug>/sucess',
         views.register_success, name="register-success"),
    path('<slug:slug>', views.meetup_detail, name='meetup-detail'),

]
