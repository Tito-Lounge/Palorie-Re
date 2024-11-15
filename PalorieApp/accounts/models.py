from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import uuid

class CustomUser(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    height_ft = models.PositiveIntegerField(null=True,blank=True)
    height_in = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True,blank=True)
    
    pass

    def __str__(self):
        return self.username

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

