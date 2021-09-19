from django.contrib import admin
from .models import Public, Workplace, AdminTask

class PublicAdmin(admin.ModelAdmin):
  search_fields = ['name', 'email']

# Register your models here.
admin.site.register(Public, PublicAdmin)
admin.site.register(Workplace)
admin.site.register(AdminTask)
