from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
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

class JSONEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='json_entries')
    json_data = models.JSONField() # Stores JSON data
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Entry for {self.user.username}"
