from django.shortcuts import redirect

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
