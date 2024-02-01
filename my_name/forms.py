from django.forms import ModelForm
from rest_framework import serializers
# myapp/forms.py
from django import forms
from .models import UserProfile

class RegistrationForm(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email',]
