from dataclasses import field, fields
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

from .models import Customer, cropprediction


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

class Meta:
    model = User 
    field = ['User', 'email', 'password1', 'password2']
    labels = {'email': 'Email'}
    widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}
    
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class MypasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
  class Meta:   
      model = Customer
      fields = ['name', 'state', 'city', 'locality', 'zipcode']
      widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}), 'city':forms.TextInput(attrs={'class':'form-control'}),'state':forms.Select(attrs={'class':'form-control'}),'zipcode':forms.NumberInput(attrs={'class':'form-control'})}

class CropPredictionForm(forms.ModelForm):
   class Meta:
        model =  cropprediction
        fields = ['state', 'district', 'year', 'season', 'crop', 'area', 'temperature', 'windspeed', 'pressure', 'humidity', 'soiltype', 'n', 'p', 'k', 'production'] 
        Widgets = {'State Name':forms.Select(attrs={'class':'form-control'}),'district':forms.Select(attrs={'class':'form-control'}),'year':forms.NumberInput(attrs={'class':'form-control'}),'season':forms.Select(attrs={'class':'form-control'}),'crop':forms.TextInput(attrs={'class':'form-control'}),'area':forms.Select(attrs={'class':'form-control'}),'temperature':forms.NumberInput(attrs={'class':'form-control'}),'windspeed':forms.NumberInput(attrs={'class':'form-control'}),'pressure':forms.NumberInput(attrs={'class':'form-control'}),'humidity':forms.NumberInput(attrs={'class':'form-control'}),'soiltype':forms.Select(attrs={'class':'form-control'}),'n':forms.NumberInput(attrs={'class':'form-control'}),'p':forms.NumberInput(attrs={'class':'form-control'}),'k':forms.NumberInput(attrs={'class':'form-control'}),'production':forms.NumberInput(attrs={'class':'form-control'})}    