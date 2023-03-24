from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Contact
from django.db import transaction


# Login and Signup forms for Job Seekers 
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email', 'class': 'w-full py-4 px-6 rounded-xl'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password', 'class': 'w-full py-4 px-6 rounded-xl'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user



class JobSeekerLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class JobSeekerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('fullname', 'email', 'password1', 'password2')
    
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your full name',
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
        user.is_active = True
        user.save()
        return user

# Login and Signup forms for Organizations
class OrganizationLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Your company email',
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
    class Meta():
        model = Contact
        fields = ('subject', 'name', 'email_address', 'message')
    
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Message Subject',
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

    message = forms.CharField(widget = forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl'
            }), max_length = 2000)
    
    @transaction.atomic
    def save(self):
        contact = super().save(commit=False)
        contact.save()
        return contact