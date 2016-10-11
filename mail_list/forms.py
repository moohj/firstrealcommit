from django import forms
from .models import MailListSignUp


class MailListSignUpForm(forms.ModelForm):
	class Meta:
		model = MailListSignUp
		fields = ( 
		"name",
		"email",
		"name_type",
	)


	
