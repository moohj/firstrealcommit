from django import forms
from .models import DataMine


class DataMineForm(forms.ModelForm):
	class Meta:
		model = DataMine
		exclude=()
