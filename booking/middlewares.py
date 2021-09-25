from django.shortcuts import redirect
from .models import Public, Workplace
from django.http import HttpResponseNotFound

# Allow access to date if only user's data is in session
class Verify():
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)

    return response

  def process_view(self, request, view_func, view_args, view_kwargs):
    if 'name' not in request.session:
      return redirect('booking-page')
    elif 'email' not in request.session:
      return redirect('booking-page')
    elif 'phone' not in request.session:
      return redirect('booking-page')
    elif 'birth' not in request.session:
      return redirect('booking-page')
    elif 'postal' not in request.session:
      return redirect('booking-page')
    else:
      return

# Vas
class Manage():
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)

    return response

  def process_view(self, request, view_func, view_args, view_kwargs):
    group = view_kwargs.get('group', None)
    code = view_kwargs.get('code', None)

    if len(str(code)) != 8:
      return HttpResponseNotFound('<div><h1>Not found</h1></div><a href="/">Go back</a>')

    if group == 'public':
      try:
        Public.objects.get(number=code)
        
        return
      except:
        return HttpResponseNotFound('<div><h1>Not found</h1></div><a href="/">Go back</a>')
    elif group == 'workplace':
      try:
        Workplace.objects.get(number=code)
        
        return
      except:
        return HttpResponseNotFound('<div><h1>Not found</h1></div><a href="/">Go back</a>')
    else:
      return HttpResponseNotFound('<div><h1>Not found</h1></div><a href="/">Go back</a>')