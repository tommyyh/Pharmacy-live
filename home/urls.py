from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home-home'),
  path('gallery/', views.gallery, name='home-gallery'),
  path('remove-message/', views.remove_message, name='home-remove-message'),
  path('today/', views.today, name='home-today'),
]