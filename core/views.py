from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView

from django.contrib import auth, messages

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
    return render(request, 'core/contact-us.html')

def about(request):
    return render(request, 'core/about-us.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() and form.fields['user_choice'].choices[1]:
            return redirect('/signup/job-seekers/')
        elif form.is_valid() and form.fields['user_choice'].choices[2]:
            return redirect('/signup/organizations/')
    else:
        form = SignUpForm()
            
    return render(request, "core/signup.html", {'form':form})

class UserLoginView(LoginView):
    
    redirect_authenticated_user = True
    template_name='core/login.html' 
    authentication_form=LoginForm

    def login(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)     
            if form.is_valid() and form.fields['user_choice'].choices[1]:
                return redirect('/login/job-sekers/')
            elif form.is_valid() and form.fields['user_choice'].choices[2]:
                return redirect('/login/organizations/')
            else:
                form = LoginForm()
                
            return render(request, "core/login.html", {'form':form})

class ApplicantSignUpView(CreateView):
    model = User
    form_class = JobSeekerSignupForm
    template_name = 'core/jobseeker-signup.html'
    success_url = '/'

    extra_context = {
        'title': 'Job-Seekers Signup'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user_type = 'job-seeker'
            user.set_password(password)
            user.save()
            return user_type, redirect('/login/job-seekers/')
        else:
            return render(request, 'core/jobseeker-signup.html', {'form': form})

class OrganizationSignUpView(CreateView):
    model = User
    form_class = OrganizationSignupForm
    template_name = 'core/organization-signup.html'
    success_url = '/'

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
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user_type = 'organization'
            user.set_password(password)
            user.save()
            return user_type, redirect('/login/organizations/')
        else:
            return render(request, 'core/organizations-signup.html', {'form': form})


class ApplicantLoginView(FormView):

    success_url = '/'
    form_class = JobSeekerLoginForm
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
    form_class = OrganizationLoginForm
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

    url = 'login/'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You have logged out successfully!')
        return super(LogoutView, self).get(request, *args, **kwargs)

