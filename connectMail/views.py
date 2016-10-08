from django.core.mail import send_mail

def contact_mail():
	if form.is_valid():
	    subject = form.cleaned_data['subject']
	    message = form.cleaned_data['message']
	    sender = form.cleaned_data['sender']
	    cc_myself = form.cleaned_data['cc_myself']

	    recipients = ['contact@epicwednesday.com']
	    if cc_myself:
	        recipients.append(sender)

	    send_mail(subject, message, sender, recipients)
	 return ('thanks')
