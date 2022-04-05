from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    template_name='store/home.html'
    
    return render(request,template_name)
