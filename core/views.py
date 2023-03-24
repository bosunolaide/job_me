from django.shortcuts import render, redirect

# from django.contrib.auth.views import LoginView

from django.contrib import auth, messages

from django.core.mail import send_mail, BadHeaderError

from django.http import HttpResponse

from django.views.generic import RedirectView, CreateView, FormView

from job.models import Category, Location, Job

from .forms import *
from .models import User

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
    form = ContactForm()
    return render(request, 'core/contact-us.html', {'form':form})

def about(request):
    return render(request, 'core/about-us.html')

def signup(request):
    return render(request, "core/signup.html")

def login(request):
    return render(request, "core/login.html")

def applicantsignup(request):
    if request.method == 'POST':
        form = JobSeekerSignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/job-seekers/')
    else:
        form = JobSeekerSignupForm()

    return render(request, 'core/jobseeker-signup.html', {
        'form': form
    })

def organizationsignup(request):
    if request.method == 'POST':
        form = OrganizationSignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/organizations/')
    else:
        form = OrganizationSignupForm()

    return render(request, 'core/organization-signup.html', {
        'form': form
    })

class OrganizationSignUpView(CreateView):
    model = User
    form_class = OrganizationSignupForm
    template_name = 'core/organization-signup.html'
    success_url = '/login/organizations/'

    extra_context = {
        'title': 'Organizations Signup'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save()
            password = form.cleaned_data['password1']
            user_type = 'organization'
            user.set_password(password)
            user.save()
            return user_type, redirect('/login/organizations/')
        else:
            return render(request, 'core/organizations-signup.html', {'form': form})


class ApplicantLoginView(FormView):

    success_url = '/'
    form_class = UserLoginForm
    template_name = 'core/jobseeker-login.html'

    extra_context = {
        'title': 'Job-Seekers Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    

class OrganizationLoginView(FormView):

    success_url = '/'
    form_class = UserLoginForm
    template_name = 'core/organization-login.html'

    extra_context = {
        'title': 'Organizations Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):

    url = '/'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You have logged out successfully!')
        return super(LogoutView, self).get(request, *args, **kwargs)
"""
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject'] 
			body = {                
			'name': form.cleaned_data['name'], 
			'email_address': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/")
      
	form = ContactForm()
	return render(request, "core/contact-us.html", {'form':form})
"""