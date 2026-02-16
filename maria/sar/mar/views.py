from django.shortcuts import render
from requests import request
def home(request):
    return render(request, 'home.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
 