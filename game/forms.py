from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label='full name')
    email = forms.EmailField(label='email')
    text = forms.CharField(label='name')
