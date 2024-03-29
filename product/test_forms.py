from django.test import TestCase
from .forms import ProductForm
from django.contrib.auth.models import User

class TestProductForm(TestCase):
    def test_title_is_required(self):
        """
        Test if title field is required.
        """
        form = ProductForm(data={
            'title': '',
            'price': 100,
            'description': 'description',
            'quantity': 1,
            'category': 'Cleanser',
        })

        self.assertFalse(
            form.is_valid(),
            msg="Title was not provided, but form is valid"
        )

    def test_price_is_required(self):
        """
        Test if price field is required.
        """
        form = ProductForm(data={
            'title': 'product',
            'price': '',
            'description': 'description',
            'quantity': 1,
            'category': 'Cleanser',
        })

        self.assertFalse(
            form.is_valid(),
            msg="Price was not provided, but form is valid"
        )

    def test_description_is_required(self):
        """
        Test if description field is required.
        """
        form = ProductForm(data={
            'title': 'product',
            'price': 100,
            'description': '',
            'quantity': 1,
            'category': 'Cleanser',
        })

        self.assertFalse(
            form.is_valid(),
            msg="Description was not provided, but form is valid"
        )

    def test_quantity_is_required(self):
        """
        Test if quantity field is required.
        """
        form = ProductForm(data={
            'title': 'product',
            'price': 100,
            'description': 'description',
            'quantity': '',
            'category': 'Cleanser',
        })

        self.assertFalse(
            form.is_valid(),
            msg="Quantity was not provided, but form is valid"
        )

    def test_category_is_required(self):
        """
        Test if category field is required.
        """
        form = ProductForm(data={
            'title': 'product',
            'price': 100,
            'description': 'description',
            'quantity': 1,
            'category': '',
        })

        self.assertFalse(
            form.is_valid(),
            msg="Category was not provided, but form is valid"
        )

    def test_seller_is_required(self):
        """
        Test if seller field is required.
        """
        form = ProductForm(data={
            'title': 'product',
            'price': 100,
            'description': 'description',
            'quantity': 1,
            'category': 'Cleanser',
            'seller': '',
        })

        self.assertFalse(
            form.is_valid(),
            msg="Seller was not provided, but form is valid"
        )