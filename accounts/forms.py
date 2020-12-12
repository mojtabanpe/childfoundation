from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField( max_length=30, required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('this email already exists!')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError('this username already exists!')
        return username

    def clean(self):
        data = super().clean()
        password = data['password']
        confirm_password = data['confirm_password']
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('passwords must match!')        