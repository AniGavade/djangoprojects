from pyexpat import model
from django import forms
from .models import users

class userForms(forms.ModelForm):
    class Meta:
        model=users
        fields= "__all__"