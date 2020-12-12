from django import forms

class ContactForm(forms.Form):
    INTREST_IN = (
        ("Tell Us How We Can Serve You","Tell Us How We Can Serve You"),
        ("Add me to your Mailing List","Add me to your Mailing List"),
        ("Information about volunteering","Information about volunteering"),
        ("I am interested in becoming a sponsor","I am interested in becoming a sponsor"),
        ("Others","Others"),
    )
    name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    country = forms.CharField(max_length=20,required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=20,required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length=20, required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=20,required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    intrest_in = forms.CharField(required=False,widget=forms.Select(choices=INTREST_IN,attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))