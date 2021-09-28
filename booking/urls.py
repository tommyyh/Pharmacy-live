from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('public/', views.booking, name='booking-page'),
    path('workplace/', views.booking, name='booking-page-workplace'),
    path('date/', views.date, name='booking-date'),
    path('new-date/', views.new_date, name='new-date'),
    path('new-user/', views.new_user, name='new-user'),
    path('book-appointment/', views.book_appointment, name='book-appointment'),
    path('workplace-status/', views.workplace_status, name='workplace-status'),
    path('manage/', views.change, name='booking-change'),
    path('check-code/', views.check_code, name='booking-check-code'),
    path('save-changes/', views.save_changes, name='booking-save-changes'),
]
