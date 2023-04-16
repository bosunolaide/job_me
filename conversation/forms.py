from django import forms

from .models import ConversationMessage

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('cover_letter', 'curriculum_vitae')
        widgets = {
            'cover_letter': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'curriculum_vitae': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }