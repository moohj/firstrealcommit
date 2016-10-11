from django.shortcuts import render
from mail_list.forms import MailListSignUpForm
from mail_list.views import signupmodal


# Create your views here.
def whatwedo(request):
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	}	
	return render(request,'infopages/whatwedo.html',context)

def whoweare(request):
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	}
	return render(request,'infopages/whoweare.html',context)

def privacypolicy(request):
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	}
	return render(request,'infopages/privacypolicy.html',context)

def  termsofuse(request):
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	}
	return render(request,'infopages/termsofuse.html',context)

def forbusiness(request):
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	}
	return render(request,'infopages/forbusiness.html',context)

def forbargoers(request):
	form = signupmodal(request)
	context = {
	"form":form["form"],
	"error":form["error"],
	}
	return render(request,'infopages/forbargoers.html',context)




