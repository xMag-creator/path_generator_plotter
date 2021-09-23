from django import forms
from django.core.exceptions import ValidationError

from machine_app.models import Machine, Tool


def validate_range(max_range, min_range):
    # check if values are correctly set
    if max_range <= min_range:
        raise ValidationError(f"min value: {min_range} is bigger that max value: {max_range}.")


def less_that_zero(value):
    # check is value is not less that zero
    if value < 0:
        raise ValidationError(f"The value {value} is less that zero.")


class AddMachineForm(forms.ModelForm):
    # form to add machine profil
    x_max_range = forms.FloatField(validators=[less_that_zero], initial=100.0)
    x_min_range = forms.FloatField(validators=[less_that_zero], initial=0.0)
    y_max_range = forms.FloatField(validators=[less_that_zero], initial=100.0)
    y_min_range = forms.FloatField(validators=[less_that_zero], initial=0.0)
    z_max_range = forms.FloatField(validators=[less_that_zero], initial=100.0)
    z_min_range = forms.FloatField(validators=[less_that_zero], initial=0.0)
    u_max_range = forms.FloatField(validators=[less_that_zero], initial=0.0)
    u_min_range = forms.FloatField(validators=[less_that_zero], initial=0.0)
    v_max_range = forms.FloatField(validators=[less_that_zero], initial=0.0)
    v_min_range = forms.FloatField(validators=[less_that_zero], initial=0.0)
    w_max_range = forms.FloatField(validators=[less_that_zero], initial=0.0)
    w_min_range = forms.FloatField(validators=[less_that_zero], initial=0.0)
    z_push_pos = forms.FloatField(validators=[less_that_zero], initial=0.0)
    z_jump_lim = forms.FloatField(validators=[less_that_zero], initial=10.0)
    x_sheet_offset = forms.FloatField(validators=[less_that_zero], initial=0.0)
    y_sheet_offset = forms.FloatField(validators=[less_that_zero], initial=0.0)
    
    class Meta:
        model = Machine
        fields = ['name',
                  'x_max_range',
                  'x_min_range',
                  'y_max_range',
                  'y_min_range',
                  'z_max_range',
                  'z_min_range',
                  'u_max_range',
                  'u_min_range',
                  'v_max_range',
                  'v_min_range',
                  'w_max_range',
                  'w_min_range',
                  'z_push_pos',
                  'z_jump_lim',
                  'x_sheet_offset',
                  'y_sheet_offset',
                  ]

    def clean(self):
        # check ranges
        cleaned_data = super(AddMachineForm, self).clean()
        validate_range(cleaned_data.get('x_max_range'), cleaned_data.get('x_min_range'))
        validate_range(cleaned_data.get('y_max_range'), cleaned_data.get('y_min_range'))
        validate_range(cleaned_data.get('z_max_range'), cleaned_data.get('z_min_range'))
        validate_range(cleaned_data.get('z_jump_lim'), cleaned_data.get('z_push_pos'))


class AddToolForm(forms.ModelForm):
    # form to add tool
    diameter = forms.FloatField(validators=[less_that_zero])

    class Meta:
        model = Tool
        fields = ['name', 'diameter', 'color']


