from allauth.account.forms import SignupForm
from allauth.account.utils import user_email
from django import forms
from django.shortcuts import redirect

class AccountSignupForm(SignupForm):

    template_name = "accounts/signup.html"
    first_name = forms.CharField(max_length=30, label='first_name')
    last_name = forms.CharField(max_length=30, label='last_name')

    def save(self, request):
        user = super(AccountSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user



