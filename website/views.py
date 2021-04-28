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


def about(request):
	context = {}
	return render(request, 'about.html', {})

def pricing(request):
	context = {}
	return render(request, 'pricing.html', {})

def service(request):
	context = {}
	return render(request, 'service.html', {})

def appointment(request):
	context = {}
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']

		appointment = your_name + " " + your_phone + " " + your_email + " " + your_name + " " + your_address + " " + your_schedule + " " +your_date + " " +your_message 

		context = {
					'your_name' :your_name,
					'your_phone' :your_phone,
					'your_email' :your_email,
					'your_address' :your_address,
					'your_schedule' :your_schedule,
					'your_date' :your_date,
					'your_message' :your_message,
					}

		send_mail(
			f"Appointment request {your_name}", # subject
			appointment, # message
			your_email, # from email
			['thrivero1@gmail.com'], # to email
			)



		return render(request, 'appointment.html', context)

	else:
		return render(request, 'home.html',{})

	

		