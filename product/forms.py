from django import forms
from .models import Product

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('seller', 'title', 'price', 'quantity','category','product_image','description')


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('seller', 'title', 'price', 'quantity','category','product_image','description')