from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from booking.models import Public, Workplace

@login_required
def admin(request):
  return render(request, 'admin/admin.html', {})

@login_required
def selected_day(request, date, group, place, sort):
  model = None
  formated_place = place.replace('-', ' ').title()
  sort_formed = ''

  # Add sorting
  if sort == 'time-chron':
    sort_formed = 'time'
  elif sort == 'time-chron-r':
    sort_formed = '-time'
  elif sort == 'name':
    sort_formed = 'name'
  elif sort == 'name-r':
    sort_formed = '-name'
  elif sort == 'youngest':
    sort_formed = 'birth_date'
  elif sort == 'oldest':
    sort_formed = '-birth_date'

  if group == 'workplace':
    model = Workplace.objects.filter(date=date, pharmacy=formated_place).order_by(sort_formed)
  else:
    model = Public.objects.filter(date=date, pharmacy=formated_place).order_by(sort_formed)

  context = {
    'public': model,
  }

  return render(request, 'admin/selected.html', context)
