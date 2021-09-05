from django import forms
from django.core.validators import ValidationError

from image_app.models import Image


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'path']
