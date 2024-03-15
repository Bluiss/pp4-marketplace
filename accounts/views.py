from django.views.generic import View
from django.shortcuts import render

class RegisterPageView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'authenticated_base.html')
        else:
            return render(request, 'register.html')
