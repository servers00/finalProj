from django import forms
from .models import TodoItems

class todoForm(forms.ModelForm):
	class Meta:
		model = TodoItems
		exclude = ['user']
	