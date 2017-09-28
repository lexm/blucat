from django import forms
from django.core.validators import validate_email
from .models import User
import bcrypt
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class RegForm(forms.Form):
    full_name = forms.CharField(label="Full Name:", max_length=45, min_length=2)
    alias = forms.CharField(label="Alias:", max_length=45, min_length=2)
    email = forms.CharField(label="Email:", max_length=255, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),label="Password:", max_length=258, min_length=8)
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),label="Confirm pw:", max_length=255, min_length=8)
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/logreg/register'
    helper.add_input(Submit('submit', 'Register'))
    def clean(self):
        form_data = self.cleaned_data
        if len(User.objects.filter(email=form_data.get('email'))) > 0:
            msg = 'User already registered'
            self.add_error('email', msg)
        if form_data.get('password') != form_data.get('confirm'):
            msg = 'Passwords do not match!'
            self.add_error('password', msg)
        return form_data

class LoginForm(forms.Form):
    email = forms.CharField(label="Email:", max_length=255, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),label="Password:", max_length=255, min_length=8)
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/logreg/login'
    helper.add_input(Submit('submit', 'Login'))
    def clean(self):
        form_data = self.cleaned_data
        if len(User.objects.filter(email=form_data.get('email'))) == 0:
            msg = 'User/Password mismatch'
            self.add_error('email', msg)
            self.add_error('password', msg)
        elif len(User.objects.filter(email=form_data.get('email'))) > 1:
            msg = 'Error 2: please contact your sysadmin'
            self.add_error('email', msg)
        else:
            user = User.objects.get(email=form_data.get('email'))
            if not bcrypt.checkpw(form_data.get('password').encode('utf-8'), user.hash.encode('utf-8')):
                msg = 'User/Password mismatch'
                self.add_error('email', msg)
                self.add_error('password', msg)
        return form_data
