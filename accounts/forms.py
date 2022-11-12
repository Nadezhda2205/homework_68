from django import forms
# from django.contrib.auth import get_user_model
# from django.core.exceptions import ValidationError



class LoginForm(forms.Form):
    '''форма для входа'''
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)

