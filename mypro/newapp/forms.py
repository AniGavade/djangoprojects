from django import forms
from .models import users

class userForms(forms.ModelForm):
    class Meta:
        model=users
        fields= "__all__"