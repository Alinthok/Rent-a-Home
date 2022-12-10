from django.shortcuts import render
from .models import Rental, Rating
from .forms import RatingForm, RatingCommentForm
from homepage.models import GeneralUser

# Create your views here.
def index(request):
    rentals = Rental.objects.all()
    return render(request, 'listofrentals/index.html', {'rentals' : rentals}) 

def details(request, slug):
    if request.method == 'POST':
        form = RatingForm(data=request.POST)
        formComment = RatingCommentForm(data=request.POST)
        if request.POST["context"] == 'addComment' and formComment.is_valid():
            formComment.instance.user = GeneralUser.objects.get(user=request.user)
            formComment.instance.rating = Rating.objects.get(id=request.POST['rating'])
            formComment.save()
        if request.POST["context"] == 'addRating' and form.is_valid():
            form.instance.user = GeneralUser.objects.get(user=request.user)
            form.instance.rental = Rental.objects.get(slug=slug)
            form.save()

    rental = Rental.objects.get(slug=slug)
    ratings = Rating.objects.filter(rental=rental)
    formRating = RatingForm()  
    formComment = RatingCommentForm()

    context = {  
        'rental' : rental,
        'ratings' : ratings,
        'formComment' : formComment,
        'formRating' : formRating,
        'generalUser' : GeneralUser.objects.get(user=request.user),
        'canAdd' : not Rating.objects.filter(rental=rental, user=GeneralUser.objects.get(user=request.user)).exists()  
    }  

    return render(request, 'listofrentals/details.html', context)