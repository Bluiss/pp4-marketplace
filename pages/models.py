from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User  # Import User model


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Cleanser', 'cleanser'),
        ('Moisturizer', 'moisturizer'),
        ('Serum', 'serum'),
        ('Sunscreen', 'sunscreen'),
        ('Mask', 'mask'),
        ('Toner', 'toner'),
        ('Exfoliant', 'exfoliant'),
        ('Eye Cream', 'eye_cream'),
        # Add more choices as needed
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pages_products')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title
