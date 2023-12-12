from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'role', 'profile_photo', 'address_line1', 'city', 'state', 'pincode']


class BlogForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = '__all__'