from django import forms
from django.contrib.auth.models import User
from .models import *

# Create your models here.
class reg_form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email','password']
        
class Post_form(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']        