# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth.forms import (
	UserCreationForm,
	AuthenticationForm,
	UserChangeForm)

from .models import Account

# Forms for profile related functionalities

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required = False)
	bio = forms.CharField(max_length = 1000, required = False, widget=forms.Textarea())

	class Meta:
		model = Account
		fields = ('username', 'email', 'bio', 'password1', 'password2', 'account_type')

class LoginForm(AuthenticationForm):
	username = forms.CharField(required = True, max_length = 255)
	password = forms.CharField(required = True, max_length = 255, widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('username', 'password')

class DeleteAccountForm():

	class Meta:
		model = Account
		fields = ()

class EditProfileForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('username','email', 'bio')
