from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Application



class UserRegistrationForm(UserCreationForm):
    email = form.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']



class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume']


class JobForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['title', 'company', 'description', 'location', 'salary']