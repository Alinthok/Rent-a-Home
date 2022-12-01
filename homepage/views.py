from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  
# Create your views here.  
  
def index(request):
    return render(request, 'homepage/index.html') 

def login_page(request):
    return render(request, 'homepage/login.html')  

def register_page(request):  
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save() 
            return redirect('/')
    else:  
        form = UserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'homepage/register.html', context)  