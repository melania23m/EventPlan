from django import forms
from django.forms import TextInput, Textarea, EmailInput, DateTimeInput, Select
from django.contrib.auth.forms import UserCreationForm
from providers.models import Provider


# from userextend.models import User


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



# class ReviewAdd(forms.ModelForm):
#     class Meta:
#         model = ProviderReview
#         fields = ['review_text', 'review_rating']
#         widgets = {
#             'review_text': TextInput(attrs={'placeholder': 'Please enter your review text', 'class': 'form-control'}),
#
#         }
#

