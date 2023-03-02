from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import JobSeekerLoginForm, OrganizationLoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact-us'),
    path('about-us/', views.about, name='about-us'),
    path('jobseeker-signup/', views.jobseeker_signup, name='jobseeker-signup'),
    path('organization-signup/', views.organization_signup, name='organization-signup'),
    path('jobseeker-login/', auth_views.LoginView.as_view(template_name='core/jobseeker-login.html', authentication_form=JobSeekerLoginForm), name='jobseeker-login'),
    path('organization-login/', auth_views.LoginView.as_view(template_name='core/organization-login.html', authentication_form=OrganizationLoginForm), name='organization-login'),
]
