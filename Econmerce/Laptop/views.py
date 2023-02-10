from django.shortcuts import render

# Create your views here.
def laptop(request):
    return render(request,'laptops/laptop1.html')


def lenovo(request):
    return render(request, 'laptops/lenobo.html')    