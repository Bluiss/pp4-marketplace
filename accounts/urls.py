from django.urls import path
from .views import RegisterPageView, edit_profile

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('edit_profile/<int:pk>/', edit_profile, name='edit_profile'),
]
