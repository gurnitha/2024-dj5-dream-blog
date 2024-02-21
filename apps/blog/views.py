# apps/blog/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals

# Create your views here.

def home_view(request):
	return render(request, 'blog/index.html')

def contact_view(request):
	return render(request, 'blog/contact.html')