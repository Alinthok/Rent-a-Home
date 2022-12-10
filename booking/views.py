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
    # return render(request, "booking/index.html", context)
    return render(request, "booking/index.html")

# @login_required(login_url = '/login')
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to DB
            return HttpResponseRedirect('/booking')  # Redirect on finish
        
    else: # if a GET (or any other method) we'll create a blank form
        form = BookingForm()

    return render(request, 'booking/form.html', {'form': form})

# @login_required(login_url = '/login')
def delete_booking(request, ID_booking):
    try:
        Booking.objects.get(id=ID_booking).delete()
    except Exception as e:
        print(e)
    finally:
        return redirect("/booking/")