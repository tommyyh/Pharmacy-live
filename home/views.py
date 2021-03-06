from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from booking.models import Public, Workplace
from django_xhtml2pdf.utils import generate_pdf
from datetime import datetime, timedelta
import csv

def home(request):
  success_msg = request.session['success'] if 'success' in request.session else ''

  return render(request, 'home/index.html', { 'success': success_msg })

def gallery(request):
  return render(request, 'home/gallery.html')

def privacy_policy(request):
  return render(request, 'home/privacyPolicy.html')

@api_view(['GET'])
def remove_message(request):
  request.session['success'] = ''

  return Response({ 'status': 200 })

@login_required
def today(request):
  current_month = datetime.now().month
  current_year = datetime.now().year
  current_day = datetime.now().day

  if len(str(current_day)) == 1:
    current_day = f'0{current_day}'

  if len(str(current_month)) == 1:
    current_month = f'0{current_month}'

  res = HttpResponse(content_type='application/pdf')
  users = Public.objects.filter(date__startswith=f'{current_year}-{current_month}-{current_day}').values('name', 'email', 'phone', 'time', 'postal_code', 'nhs_number', 'birth_date', 'date').distinct().order_by('time')

  pdf = generate_pdf('home/today.html', file_object=res, context={ 'users': users, 'count': users.count(), 'today': f'{current_year}-{current_month}-{current_day}' })

  return pdf

@login_required
def today_csv(request):
  output = []
  response = HttpResponse (content_type='text/csv')
  writer = csv.writer(response)

  current_month = datetime.now().month
  current_year = datetime.now().year
  current_day = datetime.now().day

  if len(str(current_day)) == 1:
    current_day = f'0{current_day}'

  if len(str(current_month)) == 1:
    current_month = f'0{current_month}'

  query_set = Public.objects.filter(date__startswith=f'{current_year}-{current_month}-{current_day}').order_by('time')

  #Header
  writer.writerow(['Name', 'Email', 'Phone', 'Time', 'Postal code', 'Nhs', 'Birth', 'Date'])
  for user in query_set:
    output.append([user.name, user.email, user.phone, user.time, user.postal_code, user.nhs_number, user.birth_date, user.date])
    
  #CSV Data
  writer.writerows(output)
  return response

@login_required
def today_workplace(request):
  res = HttpResponse(content_type='application/pdf')
  users = Workplace.objects.all()
  pdf = generate_pdf('home/today_workplace.html', file_object=res, context={ 'users': users })

  return pdf

@api_view(['GET'])
def pop_up(request):
  request.session['popUpRead'] = 'read'

  return Response({ 'status': 200 })

@api_view(['GET'])
def pop_up_check(request):
  pop_up = ''

  if 'popUpRead' not in request.session:
    pop_up = 'not'
  elif request.session['popUpRead'] == '':
    pop_up = 'not'
  else:
    pop_up = request.session['popUpRead']

  return Response({ 'status': 200, 'pop_up': pop_up })
