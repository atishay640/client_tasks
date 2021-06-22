from django import forms
from .models import Task, Tile

class TaskForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Task

class TileForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Tile