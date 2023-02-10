from django.shortcuts import render

# Create your views here.


def mobile(request):
    return render(request, 'mobiles/mobile.html')


def home(request):
    return render(request, 'home/home.html')
