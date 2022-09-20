from django import forms
from django.forms import TextInput, Textarea, EmailInput, DateTimeInput, Select



from todo_app.models import ToDoList


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'


        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),


        }
