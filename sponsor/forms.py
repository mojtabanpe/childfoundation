from sponsor.models import Sponsor
from django import forms

class EditProfileForm(forms.Form):
    GENDER = (
        ("mele", "Male"),
        ("femele", "Female"),
        ("other", "Other")
    )
    first_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=40,required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    company = forms.CharField(max_length=20, required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.CharField(required=False,widget=forms.Select(choices=GENDER,attrs={'class':'form-control'}))
