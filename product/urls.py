from django.urls import path
from .views import ProductList, ProductListDetail
from . import views 

app_name = 'product'


urlpatterns = [
    path('', ProductList.as_view(), name='productlist'),
    path('products/<int:pk>/', ProductListDetail.as_view(), name='product_detail'),
    path('new/', views.new, name='new')
]
