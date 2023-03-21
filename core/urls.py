from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import *
from .forms import JobSeekerLoginForm, OrganizationLoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact-us'),
    path('about-us/', views.about, name='about-us'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/job-seekers/', ApplicantSignUpView.as_view(), name='jobseeker-signup'),
    path('accounts/signup/organizations/', OrganizationSignUpView.as_view(), name='organization-signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('accounts/login/job-seekers/', ApplicantLoginView.as_view(), name='jobseeker-login'),
    path('accounts/login/organizations/', OrganizationLoginView.as_view(), name='organization-login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
