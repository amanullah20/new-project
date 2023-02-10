from django.urls import path
from . import views


urlpatterns = [

    path('lap/', views.laptop, name='laptop'),
    path('lnv/', views.lenovo, name='lenovo')
]
