from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import GeneralUserForm
# Create your views here.  
  
def index(request):
    return render(request, 'homepage/index.html') 

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/') 

    else: 
        form = AuthenticationForm()

    context = {  
        'form':form  
    }  
    return render(request, 'homepage/login.html', context) 

def logout_page(request):
    logout(request)
    return redirect('/') 

def register_page(request):  
    if request.method == 'POST':
        formUser = UserCreationForm(request.POST)  
        formGeneralUser = GeneralUserForm(request.POST)
        if formUser.is_valid() and formGeneralUser.is_valid():  
            usr = formUser.save()
            formGeneralUser.instance.user = usr
            formGeneralUser.save()
            return redirect('/')
    else:  
        formUser = UserCreationForm()  
        formGeneralUser = GeneralUserForm()
        
    context = {  
        'formUser':formUser,
        'formGeneralUser':formGeneralUser, 
    }  
    return render(request, 'homepage/register.html', context)  