from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView  # Add this import
from django.views import View
from product.models import Product 




# Create your views here.
class RegisterPageView(TemplateView): 
    template_name = "register.html"
    product = Product.objects.get(pk=1)
    context = {'product': product}
        



 