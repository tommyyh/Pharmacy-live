from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls')),
    path('contact/', include('contact.urls')),
    path('about/', include('about.urls')),
]
