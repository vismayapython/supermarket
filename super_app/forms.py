from .models import Task
from django import forms
class superforms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','price']
