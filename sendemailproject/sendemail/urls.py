from django.urls import path
from . import views

name = 'sendemail'

urlpatterns = [
    path('', views.index, name='index'),
]