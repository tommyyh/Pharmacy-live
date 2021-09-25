from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Public, Workplace, AdminTask
from datetime import datetime, timedelta
from django.utils.decorators import decorator_from_middleware
from .middlewares import Verify, Manage
from django.conf import settings
import random

if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail

def booking(request):
	name = request.session['name'] if 'name' in request.session else ''
	email = request.session['email'] if 'email' in request.session else ''
	phone = request.session['phone'] if 'phone' in request.session else ''
	birth = request.session['birth'] if 'birth' in request.session else ''
	postal = request.session['postal'] if 'postal' in request.session else ''
	nhs = request.session['nhs'] if 'nhs' in request.session else ''

	# Get todays date
	current_date = datetime.now()
	current_month = current_date.month
	current_day = current_date.day

	if len(str(current_day)) == 1:
		current_day = f'0{current_date.day}'

	if len(str(current_month)) == 1:
		current_month = f'0{current_date.month}'

	context = {
		'name': name,
		'email': email,
		'phone': phone,
		'birth': birth,
		'postal': postal,
		'nhs': nhs,
		'current_date': f'{current_date.year}-{current_month}-{current_day}',
	}

	return render(request, 'booking/booking.html', context)

@api_view(['GET'])
def workplace_status(request):
	workplace_status = AdminTask.objects.get(name='workplace')

	return Response({ 'workplace_status': workplace_status.is_open })

@decorator_from_middleware(Verify)
def date(request):
	current_month = (datetime.now() + timedelta(days=1)).month
	current_year = (datetime.now() + timedelta(days=1)).year
	current_day = (datetime.now() + timedelta(days=1)).day

	if len(str(current_day)) == 1:
		current_day = f'0{current_day}'

	if len(str(current_month)) == 1:
		current_month = f'0{current_month}'

	current_month2 = (datetime.now() + timedelta(days=8)).month
	current_year2 = (datetime.now() + timedelta(days=8)).year
	current_day2 = (datetime.now() + timedelta(days=8)).day

	if len(str(current_day2)) == 1:
		current_day2 = f'0{current_day2}'

	if len(str(current_month2)) == 1:
		current_month2 = f'0{current_month2}'

	context = {
		'current_date': f'{current_year}-{current_month}-{current_day}',
		'current_date2': f'{current_year2}-{current_month2}-{current_day2}',
	}

	return render(request, 'booking/date.html', context)

@api_view(['POST'])
def new_date(request):
	date_value = request.data['date']
	public_count = 0
	time_taken = []
	date = Public.objects.filter(date=date_value)
	time = [
		'9:00', '9:05', '9:10', '9:15', '9:20', '9:25', '9:30', '9:35', '9:40', '9:45', '9:50', '9:55', '10:00', '10:05', '10:10', '10:15', '10:20', '10:25', '10:30', '10:35', '10:40', '10:45', '10:50', '10:55',
  	'11:00', '11:05', '11:10', '11:15', '11:20', '11:25', '11:30', '11:35', '11:40', '11:45', '11:50', '11:55', '12:00', '12:05', '12:10', '12:15', '12:20', '12:25', '12:30', '12:35', '12:40', '12:45', '12:50', '12:55', '14:05', '14:10',
  	'14:15', '14:20', '14:25', '14:30', '14:35', '14:40', '14:45', '14:50', '14:55', '15:00', '15:05', '15:10', '15:15', '15:20', '15:25', '15:30', '15:35', '15:40', '15:45', '15:50', '15:55', '16:00', '16:05', '16:10',
  	'16:15', '16:20', '16:25', '16:30', '16:35', '16:40', '16:45', '16:50', '16:55', '17:00', '17:05', '17:10', '17:15', '17:20', '17:25', '17:30', '17:35', '17:40', '17:45', '17:50', '17:55', '18:00', '18:05', '18:10',
  	'18:15', '18:20', '18:25', '18:30',
	]

	if not date:
		return Response({ 'available_times': time })
	else:
		# Take all associated models and put them into a list
		for x in date:
			count = Public.objects.filter(date=date_value, time=x.time).count()
			public_count = count

			if count >= 14:
				time_taken.append(x.time)

		for y in date:
			count2 = Workplace.objects.filter(date=date_value, time=y.time).count()
			taken_left = 14 - public_count

			if count2 >= taken_left:
				time_taken.append(x.time)

			# Make a list containing only the values
			available_times = [x for x in time if x not in time_taken]

			return Response({ 'available_times': available_times })

@api_view(['POST'])
def new_user(request):
	name = request.data['name']
	email = request.data['email']
	phone = request.data['phone']
	birth = request.data['birth']
	postal = request.data['postal']
	nhs = request.data['nhs']
	pharmacy = request.data['pharmacy']

	# Check if user exists
	matching_users1 = Public.objects.filter(email=email)
	matching_users2 = Workplace.objects.filter(email=email)

	if matching_users1 or matching_users2:
		return Response({ 'status': 402 })

	request.session['name'] = name
	request.session['email'] = email
	request.session['phone'] = phone
	request.session['birth'] = birth
	request.session['postal'] = postal
	request.session['nhs'] = nhs
	request.session['pharmacy'] = pharmacy
	request.session['location'] = request.data['pathname']

	return Response({ 'status': 200 })

@api_view(['POST'])
def book_appointment(request):
	name = request.session['name']
	email = request.session['email']
	phone = request.session['phone']
	birth = request.session['birth']
	postal = request.session['postal']
	nhs = request.session['nhs']
	location = request.session['location']
	pharmacy = request.session['pharmacy']
	date = request.data['date']
	time = request.data['time']

	# Check if user exists
	matching_users1 = Public.objects.filter(email=email)
	matching_users2 = Workplace.objects.filter(email=email)

	if matching_users1 or matching_users2:
		return Response({ 'status': 402 })

	# Save to the db
	if location == 'public':
		user = Public(
			name=name, email=email, phone=phone, date=date, time=time, postal_code=postal,
			nhs_number=nhs, birth_date=birth, pharmacy=pharmacy
		)
		user.save()
	else:
		user = Workplace(
			name=name, email=email, phone=phone, date=date, time=time, postal_code=postal,
			nhs_number=nhs, birth_date=birth, pharmacy=pharmacy
		)
		user.save()

	# Clear session
	request.session['name'] = ''
	request.session['email'] = ''
	request.session['phone'] = ''
	request.session['birth'] = ''
	request.session['postal'] = ''
	request.session['nhs'] = ''
	request.session['location'] = ''
	request.session['pharmacy'] = ''

	# Save success message
	request.session['success'] = 'You Successfully Booked an Appointment'

	# Send email
	body = f"Dear {name}, \n\nIt’s confirmed, we’ll see you on {date}! Thank you for booking your flu vaccination with Rimmington’s Pharmacy. You’ll find details of your reservation enclosed below. \n\nDate: {date} \nTime: {time} \nLocation: 9 Bridge St, Bradford BD1 1RX, UK \n\nIf you need to get in touch, you can email or phone us directly. \n\n\nThanks again, \nRimmington’s Pharmacy"

	try:
		send_mail(
			'Flu Vaccination Confirmation with Rimmington’s Pharmacy',
			body,
			settings.EMAIL_HOST_USER,
			[email],
  	)
	except:
		return Response({ 'status': 200 })

	return Response({ 'status': 200 })