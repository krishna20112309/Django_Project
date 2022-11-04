from django import forms
from .models import *

# Create your models here.
class cart_form(forms.ModelForm):
    class Meta:
        model=Cartdetail
        fields=['q']



