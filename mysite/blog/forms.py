from django import forms
from lockdown.forms import LockdownForm

class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
