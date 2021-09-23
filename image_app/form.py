from django import forms

from image_app.models import Image


class AddImageForm(forms.ModelForm):
    # form to add image
    class Meta:
        model = Image
        fields = ['name', 'path']


class EditImageForm(forms.ModelForm):
    # form to add image
    class Meta:
        model = Image
        fields = ['name', ]
