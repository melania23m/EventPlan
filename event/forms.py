from django import forms
from django.forms import TextInput, DateTimeInput

from event.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event

        fields = ['name','location', 'event_date']


        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'location': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'event_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})


        }


