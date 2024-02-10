# accounts/urls.py

from django.urls import path
from .views import RegisterPageView  # Update the import

urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    # Add other URL patterns as needed
]