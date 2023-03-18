from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import *
from .forms import JobSeekerLoginForm, OrganizationLoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact-us'),
    path('about-us/', views.about, name='about-us'),
    path('signup/', views.signup, name='signup'),
    path('organization-signup/', views.organization_signup, name='organization-signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=JobSeekerLoginForm), name='login'),
    path('organization-login/', auth_views.LoginView.as_view(template_name='core/organization-login.html', authentication_form=OrganizationLoginForm), name='organization-login'),
    path('logout', LogoutView.as_view(), name='logout')
]
