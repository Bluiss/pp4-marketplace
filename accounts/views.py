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
        return user_profile


def edit_profile(request ,pk):
    user_profile = UserProfile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=user_profile)
    if form.is_valid():
        form.save()
        messages.success(request, "Profile edited")
        return redirect('accounts:register')
    return render(request, 'accounts/edit_profile.html', {'form': form})

