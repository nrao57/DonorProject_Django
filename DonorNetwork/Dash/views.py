from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Dash.forms import UserForm, UserProfileForm
from Dash.helpers import safe_get

def index(request):
    context = RequestContext(request)
    return render_to_response('Dash/index.html')

def home(request):
    context_dict = safe_get(request)
    return render(request, 'Dash/homepage.html', context=context_dict)

def contact(request):
    context_dict = safe_get(request)
    return render(request, 'Dash/contact.html', context=context_dict)

def about(request):
    context_dict = safe_get(request)
    return render(request, 'Dash/about.html', context=context_dict)

def pricing(request):
    context_dict = safe_get(request)
    return render(request, 'Dash/pricing.html', context=context_dict)

def thank_you(request):
    context_dict = safe_get(request)
    return render(request, 'Dash/thank_you.html', context=context_dict)

def demo(request):
    context_dict = safe_get(request)
    return render(request, 'Dash/demo.html', context = context_dict)


def profile(request):
    context_dict = {}
    u = User.objects.get(username=request.user)
    try:
        up = UserProfile.objects.get(user=u)
    except:
        up = None

    context_dict['user'] = u
    context_dict['userprofile'] = up
    return render(request, 'Dash/profile.html', context=context_dict)

def features(request):
    context_dict = safe_get(request)
    return render(request, 'Dash/features.html', context=context_dict)

# Not needed because django has built-in forms and views for usercreation
def register(request):
    context_dict = safe_get(request)
    return render(request, 'Registration/register.html', context=context_dict)
def login(request):
    context_dict = safe_get(request)
    return render(request, 'Registration/login.html', context=context_dict)


 
