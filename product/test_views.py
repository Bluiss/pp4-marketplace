from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .views import ProductList
from .models import Product

class TestProductList(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345',
            email="test@test.com")
        self.product = Product.objects.create(
            title="Test Product",
            description="Test Description",
            price=100,
            quantity=10,
            category="Cleanser",
            seller=self.user)

    def test_product_list_view(self):
        response = self.client.get(reverse('product:productlist'))  # Correct reverse lookup
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")  # Check if product title is in response content
        self.assertContains(response, "Test Description")  # Check if product description is in response content
        self.assertIsInstance(response.context['product_list'][0], Product)  # Correct context key
