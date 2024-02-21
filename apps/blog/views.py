# apps/blog/views.py

# Django and third parties modules
from django.shortcuts import render
from django.http import HttpResponse

# Locals

# Create your views here.

def home_view(request):
	return HttpResponse('Hallo World!')