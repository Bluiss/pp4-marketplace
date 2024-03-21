from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Product 

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product) 
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")