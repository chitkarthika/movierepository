from django import forms
from .models import mymovie
class movieform(forms.ModelForm):
    class Meta:
        model=mymovie
        fields=['name','desc','year','img']

