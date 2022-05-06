from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Full Name", 'maxlength': 25}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "Email Address"}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Subject Line"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "Message", 'rows': 5, 'style': "height: 10rem"}))
