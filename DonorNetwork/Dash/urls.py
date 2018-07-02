from django.urls import path, re_path, reverse_lazy
from django.conf.urls import url
from Dash import views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [

    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    re_path(r'^about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('features/', views.features, name='features'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('demo/', views.demo, name='demo'),
	path('login/', views.login, name='login'),	
	path('register/', views.register, name='register'),
]
