from django.shortcuts import render

# Create your views here.


def cloth(request):
    return render(request, 'cloths/cloth1.html')
