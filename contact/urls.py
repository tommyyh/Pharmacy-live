from django.urls import path
from . import views

urlpatterns = [
  path('', views.contact, name='contact'),
  path('send-message/', views.send_email, name='contact-send'),
]