from django import forms
from .models import totalHours

class hoursForm(forms.ModelForm):
	class Meta:
		model = totalHours
		exclude = ['user']