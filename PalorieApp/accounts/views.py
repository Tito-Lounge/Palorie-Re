# accounts/views.py
from django.urls import reverse_lazy, reverse 
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect
from django.template import loader

from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import CustomUserCreationForm
from .models import JSONEntry
from django.conf import settings
from .palorieUtils import generate_from_image
import os

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

# Method for taking image input and generating an entry
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
        
        # Process the image and output the intermediary JSON string
        json_data = generate_from_image(upload_path)
        
        # Save the JSON entry associated with the user
        
        entry = save_json_entry(request.user, json_data)

        # Make sure to delete image

        # Forward to page displaying entry information. (change redirect later)
        return HttpResponse("Image uploaded and processed successfully!")
    return HttpResponse("Failed to upload and process image.")

# Methods for saving JSON entry
def save_json_entry(user, json_data):
    entry = JSONEntry.objects.create(user=user,json_data=json_data)
    return entry

# Method for listing JSON entries for a user
@login_required
def user_json_entries(request):
    user = request.user
    entries = user.json_entries.all()
    print(f"Logged-in user: {request.user} ({type(request.user)})")
    print(entries)
    return render(request, 'user_entries.html', {
        'entries': entries,
        'user' : request.user,
        })