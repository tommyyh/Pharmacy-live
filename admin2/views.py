from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from booking.models import Public, Workplace
from rest_framework.decorators import api_view
from rest_framework.response import Response

@login_required
def admin(request):
  return render(request, 'admin/admin.html', {})

@login_required
def selected_day(request, date, group, place):
  model = None
  formated_place = place.replace('-', ' ').title()

  if group == 'workplace':
    model = Workplace.objects.filter(date=date, pharmacy=formated_place)
  else:
    model = Public.objects.filter(date=date, pharmacy=formated_place)

  context = {
    'public': model,
  }

  return render(request, 'admin/selected.html', context)
