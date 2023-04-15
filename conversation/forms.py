from django import forms

from .models import ConversationMessage, CVModel

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('cover_letter')
        widgets = {
            'cover_letter': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            })
            
        }


class UploadCVForm(forms.ModelForm):
    class Meta:
        model = CVModel
        fields = ('curriculum_vitae')
        widget = {
            'curriculum_vitae': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })

        }