from django.shortcuts import render
from .models import BusinesSignUp
from .forms import BusinesSignUpForm

import requests
import json

# Create your views here.
def index(request):
	print(request.method)

	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	"url_base":'http://www.epicwednesday.com/',
	}
	return render(request,'businesslocation/index.html', context)


def signupmodal(request_):
	# if this is a POST request_ we need to process the form data
	error = ""
	if request_.method == 'POST':
		# create a form instance and populate it with data from the request_:
		form = BusinesSignUpForm(request_.POST )

		# check whether it's valid:
		if form.is_valid():
			print('form is valid')

			form.save()
		else :
			form = BusinesSignUpForm()

				# process the data in form.cleaned_data as required
				# ...
				# redirect to a new URL:
			
	# if a GET (or any other method) we'll create a blank form
	else:
		print("not post")
		form = BusinesSignUpForm()
	output = {
	"error":error,
	"form":form,
	}
	
	return output
