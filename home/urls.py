from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home-home'),
  path('gallery/', views.gallery, name='home-gallery'),
  path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
  path('remove-message/', views.remove_message, name='home-remove-message'),
  path('today-workplace/', views.today_workplace, name='home-today'),
  path('today-public/', views.today, name='home-today-workplace'),
  path('today-public-csv/', views.today_csv, name='home-today-csv'),
  path('pop-up-read/', views.pop_up, name='pop-up-read'),
  path('pop-up-check/', views.pop_up_check, name='pop-up-check'),
]