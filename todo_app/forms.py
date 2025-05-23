from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Task title', 'class': 'input-box'}),
            'description': forms.Textarea(attrs={'placeholder': 'Task description', 'class': 'input-box', 'rows': 4}),
        }