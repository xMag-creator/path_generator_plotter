from django import forms

from project_app.models import Project


class AddProjectForm(forms.ModelForm):
    # form for adding new project
    class Meta:
        model = Project
        fields = ['name',
                  'image',
                  'machine',
                  'tool',
                  'sheet_width',
                  'sheet_height',
                  'image_position_x',
                  'image_position_y',
                  'image_size',
                  'image_rotation',
                  ]
