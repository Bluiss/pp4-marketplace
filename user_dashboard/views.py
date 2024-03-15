from django.shortcuts import render
from django.views import generic
from .models import UserProfile
from django.contrib.auth.models import DetailView


# Create your views here.
class UserProfileDash(generic.DetailView):
    model = UserProfile
    template_name = "register.html"

