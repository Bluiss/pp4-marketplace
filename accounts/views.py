from django.views.generic import DetailView
from .models import UserProfile

class RegisterPageView(DetailView):
    template_name = 'register.html'
    model = UserProfile
    context_object_name = 'user_profile'
    
    def get_object(self, queryset=None):
        # Retrieve the UserProfile object associated with the current user
        return self.request.user.userprofile
