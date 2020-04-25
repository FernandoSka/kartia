from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100, required=True)
    password = forms.CharField(label='Your password', max_length=100, required=True)