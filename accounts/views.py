from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib import messages


class RegisterPageView(LoginRequiredMixin, DetailView):
    template_name = 'register.html'
    model = UserProfile
    context_object_name = 'user_profile'
    
    def get_object(self, queryset=None):
        user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return self.request.user.userprofile


def new_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            messages.success(request, "Profile uploaded")
            return redirect('register')  # Redirect to register page
    else:
        form = ProfileForm()

    return render(request, 'accounts/new.html', {'form': form})
