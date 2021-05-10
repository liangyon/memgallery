from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import MyUser, ImageModel


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('email',)


class Imageform(forms.Form):
    """form for images"""
    img_text = forms.CharField(label='Description', max_length=200)
    img = forms.ImageField()
    user = None