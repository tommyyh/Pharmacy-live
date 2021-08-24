from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from booking.models import User
from django_xhtml2pdf.utils import generate_pdf

def home(request):
  success_msg = request.session['success'] if 'success' in request.session else ''

  return render(request, 'home/index.html', { 'success': success_msg })

@api_view(['GET'])
def remove_message(request):
  request.session['success'] = ''

  return Response({ 'status': 200 })

@login_required
def today(request):
  res = HttpResponse(content_type='application/pdf')
  users = User.objects.all()
  pdf = generate_pdf('home/today.html', file_object=res, context={ 'users': users })

  return pdf