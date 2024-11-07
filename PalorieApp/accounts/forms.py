from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField(required=False, min_value=0, label="Age")
    height_ft = forms.IntegerField(required=False, min_value=0, max_value=8, label="Height (ft)")
    height_in = forms.IntegerField(required=False, min_value=0, max_value=11, label="Height (in)")
    weight = forms.FloatField(required=False, min_value=0, label="Weight (lbs)")
    first_name = forms.CharField(max_length=30, required=False, label="First Name")
    last_name = forms.CharField(max_length=30, required=False, label="Last Name")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'height_ft', 'height_in', 'weight')

    def save(self, commit=True):
        user = super().save(commit=False)
        # Save custom fields
        user.age = self.cleaned_data.get('age')
        user.height_ft = self.cleaned_data.get('height_ft')
        user.height_in = self.cleaned_data.get('height_in')
        user.weight = self.cleaned_data.get('weight')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    age = forms.IntegerField(required=False, min_value=0, label="Age")
    height_ft = forms.IntegerField(required=False, min_value=0, max_value=8, label="Height (ft)")
    height_in = forms.IntegerField(required=False, min_value=0, max_value=11, label="Height (in)")
    weight = forms.FloatField(required=False, min_value=0, label="Weight (lbs)")
    first_name = forms.CharField(max_length=30, required=False, label="First Name")
    last_name = forms.CharField(max_length=30, required=False, label="Last Name")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'height_ft', 'height_in', 'weight')

    def save(self, commit=True):
        user = super().save(commit=False)
        # Update custom fields
        user.age = self.cleaned_data.get('age')
        user.height_ft = self.cleaned_data.get('height_ft')
        user.height_in = self.cleaned_data.get('height_in')
        user.weight = self.cleaned_data.get('weight')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        
        if commit:
            user.save()
        return user