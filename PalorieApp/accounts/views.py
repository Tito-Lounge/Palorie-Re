# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import CustomUserCreationForm

# Form for User Creation
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# Simple Logout Redirect
def custom_logout_view(request):
    logout(request)
    return redirect('')