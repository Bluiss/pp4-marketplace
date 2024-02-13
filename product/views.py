from django.shortcuts import render
from django.views import generic
from .models import Product

class ProductList(generic.ListView):
    model = Product
    template_name = "product.html"
    paginate_by = 6

class ProductListDetail(generic.DetailView):
    model = Product
    template_name = "product_detail.html"
