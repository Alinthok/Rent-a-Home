from django.shortcuts import render
from .forms import Form
from django.http.response import HttpResponseRedirect

# Create your views here.
def index(request):
    form = Form(request.POST)
    if request.method == 'POST'and form.is_valid():
        form.save()
        return HttpResponseRedirect ('/')
    else:
        form = Form
    return render(request, "addarental.html", {"form":form})