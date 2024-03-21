# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('delete/<int:product_id>/', views.delete_cart, name='delete_cart'),
    # Other URL patterns for your cart app...
]
