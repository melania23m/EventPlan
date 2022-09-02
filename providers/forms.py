from django import forms
from django.forms import TextInput, Textarea, EmailInput, DateTimeInput, Select

from providers.models import Provider


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider

        fields = ['name','email','city', 'description', 'image']


        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'city': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control'}),


        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control'
