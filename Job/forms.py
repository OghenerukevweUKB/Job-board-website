from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Application, Job


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['Email', 'Location', 'Years_of_experience', 'Why_you_are_fit_for_the_job', 'Position_applying_to', 'Resume']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['Title', 'Company', 'Description', 'Location', 'Salary']
