from django.urls import path
from . import views

urlpatterns = [
  path('', views.admin, name='admin'),
  path('day/<str:date>/<str:group>/<str:place>/<str:sort>', views.selected_day, name='admin-selected'),
]