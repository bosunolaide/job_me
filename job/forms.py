from django import forms

from .models import Job

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('category', 'location', 'name', 'description', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'location': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('name', 'description', 'image', 'is_filled')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }