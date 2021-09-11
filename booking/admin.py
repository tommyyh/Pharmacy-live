from django.contrib import admin
from .models import Public, Workplace, AdminTask

# Register your models here.
admin.site.register(Public)
admin.site.register(Workplace)
admin.site.register(AdminTask)
