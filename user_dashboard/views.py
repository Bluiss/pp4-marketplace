from django.views.generic import DetailView
from .models import UserProfile

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'authenticated_base.html'  
    context_object_name = 'user_profile'  
