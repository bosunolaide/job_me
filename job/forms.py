from django import forms

from .models import Job

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('category', 'location', 'job_title', 'job_description', 'company_logo',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'location': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'job_title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'job_description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'company_logo': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('job_title', 'job_description', 'company_logo', 'is_filled')
        widgets = {
            'job_title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'job_description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'company_logo': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }