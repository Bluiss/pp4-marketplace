from django.urls import path
from .views import UserProfileDash



urlpatterns = [
    path('', UserProfileDash.as_view(), name='UserProfileDash'),
]
