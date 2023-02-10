from django.urls import path
from . import views


urlpatterns = [

    path('mbl/', views.mobile, name='mobile'),
    path('home/', views.home, name='home')
]
