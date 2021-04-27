from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	context = {}
	return render(request, 'home.html', {})

def contact(request):
	context = {}
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send email
		send_mail(
			f"Message from {message_name}", # subject
			message, # message
			message_email, # from email
			['thrivero1@gmail.com'], # to email
			)

		context = {
			"message_name":message_name,
		}

	return render(request, 'contact.html', context)


	

		