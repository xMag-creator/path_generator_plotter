from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator


class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=128)
    email = forms.CharField(widget=forms.EmailInput, validators=[EmailValidator(message='Wrong e-mail.')])

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password',
                  'email',
                  ]
