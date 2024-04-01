from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'name',
            'date_of_birth',
            'country',
            'phone_number',
            'address'
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }
