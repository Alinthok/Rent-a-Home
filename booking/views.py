from django.http import response
from django.shortcuts import redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm

# Create your views here.
# @login_required(login_url = '/login')
def index(request):
    # context = {"user_id": request.user.id}
    # return render(request, "agenda_main.html", context)
    return render(request, "homepage/index.html")

# @login_required(login_url = '/login')
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to DB
            return HttpResponseRedirect('/booking')  # Redirect on finish
        
    else: # if a GET (or any other method) we'll create a blank form
        form = BookingForm()

    return render(request, 'form.html', {'form': form})