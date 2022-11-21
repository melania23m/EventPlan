from django import forms
from django.forms import TextInput, Textarea, EmailInput, DateTimeInput, Select, FloatField, CharField

from todo_app.models import ToDoList, Budget


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),

        }


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget

        fields = ['denumire','avans','cost_total']

        widgets = {
            'denumire': TextInput({'class': 'form-control'}),
            'avans': TextInput({'class': 'form-control'}),
            'cost_total': TextInput({'class': 'form-control'}),

        }



