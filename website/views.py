from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def team(request):
	return render(request, 'team.html', {})

def contact_us(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		phone_number = request.POST['phone-number']
		message = request.POST['message']

		# send an email
		send_mail(
    		'message from ' + message_name,
    		message +  ('  This is my phone number:  ') + phone_number + ('  This is my email:  ') + message_email,
    		message_email,
    		['jonathanmedina1224@gmail.com'],
			)

		return render(request, 'contact_us.html', {'message_name': message_name})

	else:
		return render(request, 'contact_us.html', {})

def about_us(request):
	return render(request, 'about_us.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def services(request):
	return render(request, 'services.html', {})