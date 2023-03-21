from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Contact
from django.db import transaction

USER_CHOICES = [
    (1, 'Job Seeker'),
    (2, 'Organization'),
]

class SignUpForm(forms.Form):
    user_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=USER_CHOICES)

class LoginForm(forms.Form):
    user_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=USER_CHOICES)

# Login and Signup forms for Job Seekers 
class JobSeekerLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class JobSeekerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_applicant = True
        user.save()
        return user

# Login and Signup forms for Organizations
class OrganizationLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your company name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class OrganizationSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('companyname', 'email', 'password1', 'password2')
    
    companyname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your company name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_organization = True
        user.save()
        return user

class ContactForm(forms.Form):
    class Meta(forms.Form.Meta):
        model = Contact
        fields = ('title', 'name', 'email', 'message')
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Message Title',
        'class': 'w-full py-4 px-6 rounded-xl'
    }), max_length = 100)

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your full name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }), max_length = 80)

    email_address = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }),max_length = 150)

    message = forms.TextField(widget = forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl'
            }), max_length = 2000)