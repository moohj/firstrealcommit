from django.shortcuts import render
from businesslocation.forms import BusinesSignUpForm
from businesslocation.views import signupmodal
from connectMail.forms import ContactForm

# Create your views here.
def whatwedo(request):
	contactform = ContactForm()
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	"contactform":contactform,
	}	
	return render(request,'infopages/whatwedo.html',context)

def whoweare(request):
	contactform = ContactForm()
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	"contactform":contactform,
	}
	return render(request,'infopages/whoweare.html',context)

def privacypolicy(request):
	contactform = ContactForm()
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	"contactform":contactform,
	}
	return render(request,'infopages/privacypolicy.html',context)

def  termsofuse(request):
	contactform = ContactForm()
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	"contactform":contactform,
	}
	return render(request,'infopages/termsofuse.html',context)

def forbusiness(request):
	contactform = ContactForm()
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	"contactform":contactform,
	}
	return render(request,'infopages/forbusiness.html',context)

def forbargoers(request):
	contactform = ContactForm()
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	"contactform":contactform,
	}
	return render(request,'infopages/forbargoers.html',context)




