# accounts/views.py
from django.urls import reverse_lazy, reverse 
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect
from django.template import loader

from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# For image uploads
from django.conf import settings
from django.core.files.storage import default_storage 
from django.core.files.base import ContentFile
from mimetypes import guess_extension, guess_type

from .forms import CustomUserCreationForm
import os, datetime, json

# Form for User Creation
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# Simple Logout Redirect
def custom_logout_view(request):
    logout(request)
    return redirect('')

# Method for taking text input and generating an entry
@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        image_file = request.FILES['file']
        upload_filename = f"{image_file.name}"
        
        # Define path to save the uplaoded image
        upload_path = os.path.join(settings.BASE_DIR, 'uploads', upload_filename)
        
        # Save the image to a specified path
        with open(upload_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        # Process the image and return it to an entry:
        return HttpResponse("Image uploaded successfully!")
    return HttpResponse("Failed to upload image.")

# Method for taking image input and generating an entry

# Method for taking entry, assigning it to a user and storing it in a list

# Method for parsing and displaying an entry list for a user