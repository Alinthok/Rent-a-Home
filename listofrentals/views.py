from django.shortcuts import render
from .models import Rental, Rating
from .forms import RatingForm
from homepage.models import GeneralUser

# Create your views here.
def index(request):
    rentals = Rental.objects.all()
    return render(request, 'listofrentals/index.html', {'rentals' : rentals}) 

def details(request, slug):
    if request.method == 'POST':
        form = RatingForm(data=request.POST)
        if form.is_valid():
            form.instance.user = GeneralUser.objects.get(user=request.user)
            form.instance.rental = Rental.objects.get(slug=slug)
            form.save()

    rental = Rental.objects.get(slug=slug)
    ratings = Rating.objects.filter(rental=rental)
    formComment = RatingForm()  

    context = {  
        'rental' : rental,
        'ratings' : ratings,
        'formComment' : formComment,  
    }  

    return render(request, 'listofrentals/details.html', context)