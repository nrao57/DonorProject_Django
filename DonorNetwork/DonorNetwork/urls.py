from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from django.urls.conf import include
from django.contrib.auth import views as auth_views


from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

admin.autodiscover()

urlpatterns = [
    re_path(r'^&', include('Dash.urls')),
    re_path(r'^Dash/', include('Dash.urls')),
    re_path(r'^admin/', admin.site.urls),
    #path('login/', auth_views.LoginView.as_view(template_name='Registration/login.html')),
	#path('register/', auth_views.LoginView.as_view(template_name='Registration/register.html')),
    #path('accounts/', include('django.contrib.auth.urls')),
]


