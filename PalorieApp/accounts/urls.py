# accounts/urls.py
from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('accounts/logout', views.custom_logout_view),
]