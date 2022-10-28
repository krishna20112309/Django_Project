from django import forms

from firstapp.models import *

# Create your models here.
# class Post_form(forms.Form):
#     title = forms.CharField(max_length=20)
#     message = forms.CharField(widget=forms.Textarea)
   
class student_form(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
    
    