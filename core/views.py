from django.shortcuts import render, redirect

from django.contrib import auth, messages

from django.views.generic import RedirectView

from job.models import Category, Location, Job

from .forms import JobSeekerSignupForm, OrganizationSignupForm

def index(request):
    jobs = Job.objects.filter(is_filled=False)[0:6]
    categories = Category.objects.all()
    locations = Location.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'locations': locations,
        'jobs': jobs,
    })

def contact(request):
    return render(request, 'core/contact-us.html')

def about(request):
    return render(request, 'core/about-us.html')

def signup(request):
    if request.method == 'POST':
        form = JobSeekerSignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = JobSeekerSignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def organization_signup(request):
    if request.method == 'POST':
        form = OrganizationSignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/organization-login/')
    else:
        form = OrganizationSignupForm()

    return render(request, 'core/organization-signup.html', {
        'form': form
    })

class LogoutView(RedirectView):

    url = '/login/'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You have logged out successfully!')
        return super(LogoutView, self).get(request, *args, **kwargs)

