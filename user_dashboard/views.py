from django.shortcuts import render
from django.views import generic
from .models import UserProfile

# Create your views here.
class UserProfileDash(generic.ListView):
    model = UserProfile
    template_name = "register.html"

