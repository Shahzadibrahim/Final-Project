from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Home, Concepts


def home(request):
	data = Home.objects.all()
	return render(request, 'index.html', {'data': data})

def about(request):
	return render(request, 'about.html')

def concepts(request):
	# return render(request, 'concepts.html')
	data = Concepts.objects.all()
	return render(request, 'concepts.html', {'data': data})

def customers(request):
	return render(request, 'customers.html')

def shows(request):
	return render(request, 'shows.html')

def events(request):
	return render(request, 'events.html')

def contact(request):
	return render(request, 'contact.html')

	# template_name = "contact.html"
	# def post(self, request):
	# 	name = request.POST.get("text")
	# 	eml = request.POST.get("email")
	# 	msgs = request.POST.get("message")
	#
	# 	eml = EmailMessage(
	# 		subject= f"{name} from customer.",
	# 		body=msgs,
	# 		from_email=settings.EMAIL_HOST_USER,
	# 		to=[settings.EMAIL_HOST_USER],
	# 		reply_to=[eml]
	# 	)
	# 	return HttpResponse("Email sent successfully")



