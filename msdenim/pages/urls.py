from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('about', views.about, name='about'),
	path('concepts', views.concepts, name='concepts'),
	path('customers', views.customers, name='customers'),
	path('shows', views.shows, name='shows'),
	path('events', views.events, name='events'),
	path('contact', views.contact, name='contact'),
]