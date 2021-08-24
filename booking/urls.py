from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking-page'),
    path('date/', views.date, name='booking-date'),
    path('new-date/', views.new_date, name='new-date'),
    path('new-user/', views.new_user, name='new-user'),
    path('book-appointment/', views.book_appointment, name='book-appointment'),
]
