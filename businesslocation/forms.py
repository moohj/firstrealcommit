from django import forms
from .models import BusinesSignUp


class BusinesSignUpForm(forms.ModelForm):
	class Meta:
		model = BusinesSignUp
		fields = ( 
		"name",
		"email",
		"name_type",
	)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
	

