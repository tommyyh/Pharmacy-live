from django.shortcuts import redirect

# Allow access to date if only user's data is in session
class Verify():
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)

    return response

  def process_view(self, request, view_func, view_args, view_kwargs):
    name = request.session['name']
    email = request.session['email']
    phone = request.session['phone']

    if not name or not email or not phone:
      return redirect('booking-page')
    else:
      return