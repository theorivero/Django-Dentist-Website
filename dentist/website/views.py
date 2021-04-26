from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	context = {}
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		context = {
			"message_name":message_name,
		}

	return render(request, 'contact.html', context)


	

		