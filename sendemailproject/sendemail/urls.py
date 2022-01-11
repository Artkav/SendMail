from django.urls import path
from . import views

app_name = 'sendemail'

urlpatterns = [
    path('', views.index, name='index'),
    path('send_email/', views.send_email, name='send-email')
]