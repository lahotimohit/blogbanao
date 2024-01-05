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

class AppointmentForm(forms.Form):
    Doctor = forms.CharField()
    speciality = forms.CharField()
    appointment_date = forms.DateTimeField(widget=forms.DateInput,input_formats=['%Y/%m/%d %H:%M'], required=True)
    appointment_time = forms.DateTimeField(widget=forms.DateInput,input_formats= ['%Y/%m/%d %H:%M'], required=True)