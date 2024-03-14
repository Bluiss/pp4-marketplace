from django.urls import path
from .views import ProductList, ProductListDetail, DeletePost
from . import views 

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='productlist'),
    path('products/<int:pk>/', ProductListDetail.as_view(), name='product_detail'),
    path('new/', views.new, name='new'),
    path('edit/<int:model_id>/', views.edit, name='edit'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),
]
