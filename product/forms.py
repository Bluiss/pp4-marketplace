from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('seller', 'title', 'price', 'quantity','category','product_image','description')


