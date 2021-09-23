from django import forms
from django.core.exceptions import ValidationError

from project_app.models import Project


def less_that_zero(value):
    # check is value is not less that zero
    if value < 0:
        raise ValidationError(f"The value {value} is less that zero.")


def totally_out_of_area(lower_value, bigger_value):
    # check is image is totally out of work area
    if lower_value > bigger_value:
        raise ValidationError('Image out of work area.')


def little_out_of_area(sheet, pos, size):
    # check is image is little out of work area
    if sheet < pos + size:
        raise ValidationError('Image out of work area.')


class AddProjectForm(forms.ModelForm):
    # form for adding new project
    sheet_width = forms.FloatField(validators=[less_that_zero], initial=210)
    sheet_height = forms.FloatField(validators=[less_that_zero], initial=297)
    image_position_x = forms.FloatField(validators=[less_that_zero], initial=0)
    image_position_y = forms.FloatField(validators=[less_that_zero], initial=0)
    image_size = forms.FloatField(validators=[less_that_zero], initial=100)

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

    def clean(self):
        # checking is image fit in to work area
        cleaned_data = super(AddProjectForm, self).clean()
        h_image_size = self.calculate_resolution() * self.image.height

        totally_out_of_area(cleaned_data.get('image_position_x'), cleaned_data.get('sheet_width'))
        totally_out_of_area(cleaned_data.get('image_position_y'), cleaned_data.get('sheet_height'))

        little_out_of_area(cleaned_data.get('sheet_width'),
                           cleaned_data.get('image_position_x'),
                           cleaned_data.get('image_size'))
        little_out_of_area(cleaned_data.get('sheet_height'), cleaned_data.get('image_position_y'), h_image_size)
