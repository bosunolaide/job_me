from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import *
from .forms import JobSeekerLoginForm, OrganizationLoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact-us'),
    path('contact-thanks/', views.contact_thanks, name='contact-thanks'),
    path('about-us/', views.about, name='about-us'),
    path('signup/', views.signup, name='signup'),
    path('signup/job-seekers/', views.applicantsignup, name='jobseeker-signup'),
    path('signup/organizations/', views.organizationsignup, name='organization-signup'),
    path('login/', views.login, name='login'),
    path('login/job-seekers/', ApplicantLoginView.as_view(), name='jobseeker-login'),
    path('login/organizations/', OrganizationLoginView.as_view(), name='organization-login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
