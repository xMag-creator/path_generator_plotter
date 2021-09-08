from django import forms

from project_app.models import Project


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'machine']
