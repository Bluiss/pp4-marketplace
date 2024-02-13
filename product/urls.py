from django.urls import path
from .views import ProductList, ProductListDetail

urlpatterns = [
    path('', ProductList.as_view(), name='productlist'),
    path('products/<int:pk>/', ProductListDetail.as_view(), name='product_detail'),
]
