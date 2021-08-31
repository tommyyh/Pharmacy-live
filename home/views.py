from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from booking.models import Public, Workplace
from django_xhtml2pdf.utils import generate_pdf

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
  res = HttpResponse(content_type='application/pdf')
  users = Public.objects.all()
  pdf = generate_pdf('home/today.html', file_object=res, context={ 'users': users })

  return pdf

@login_required
def today_workplace(request):
  res = HttpResponse(content_type='application/pdf')
  users = Workplace.objects.all()
  pdf = generate_pdf('home/today_workplace.html', file_object=res, context={ 'users': users })

  return pdf