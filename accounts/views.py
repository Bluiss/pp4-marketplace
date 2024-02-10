from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView  # Add this import

# Create your views here.
class RegisterPageView(TemplateView): 
    template_name = "register.html"
