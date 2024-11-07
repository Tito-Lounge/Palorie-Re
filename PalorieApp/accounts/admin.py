from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'age', 'height_ft', 'height_in', 'weight')
    search_fields = ('username', 'first_name', 'last_name')

admin.site.register(CustomUser, CustomUserAdmin)