from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.conf import settings

def contact(request):  
  return render(request, 'contact/contact.html')

@api_view(['POST'])
def send_email(request):
  name = request.data['name']
  email_address = request.data['email']
  msg = request.data['msg']
  body = f'Name: {name}, Email: {email_address}, Message: {msg}'

  print('fgewfewf')
  print(body)

  email = EmailMessage(
    'Rimmingtons - Contact Us',
    body,
    settings.EMAIL_HOST_USER,
    ['tommyyhoangg@gmail.com'],
  )

  email.fail_silently = False
  email.send()

  return Response({ 'status': 200 })