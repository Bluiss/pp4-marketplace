from django import forms

from .models import Product

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('seller', 'title', 'description', 'price', 'quantity','product_image')

