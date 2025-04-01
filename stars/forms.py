from django import forms
from django.core.exceptions import ValidationError
from .models import Star
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')

class StarForm(forms.ModelForm):
   """Форма для добавления знаменитости"""

   class Meta:
       model = Star
       fields = ['name', 'country', 'categories', 'birth_date', 'content', 'photo']
       widgets = {
           'name': forms.TextInput(attrs={'class': 'form-control'}),
           'country': forms.Select(attrs={'class': 'form-select'}),
           'categories': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '3'}),
           'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
           'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
           'photo': forms.FileInput(attrs={'class': 'form-control'}),
       }