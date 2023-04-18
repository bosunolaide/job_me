from django import forms
from .models import Library


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewCVForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ('full_name', 'curriculum_vitae', 'job_title', 'category', 'location', 'applicant_image')

        widgets = {

            'full_name': forms.TextInput(attrs={
                'placeholder': 'Your full name',
                'class': INPUT_CLASSES
            }),
            'curriculum_vitae': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'job_title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'location': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'applicant_image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }



class EditCVForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ('full_name', 'curriculum_vitae', 'category', 'location', 'applicant_image', 'is_employed')

        widgets = {

            'full_name': forms.TextInput(attrs={
                'placeholder': 'Your full name',
                'class': INPUT_CLASSES
            }),
            'curriculum_vitae': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'job_title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'location': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'applicant_image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
