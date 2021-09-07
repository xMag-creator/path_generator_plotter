from django import forms

from machine_app.models import Machine, Tool


class AddMachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name',
                  'x_max_range',
                  'y_max_range',
                  'z_max_range',
                  'u_max_range',
                  'u_min_range',
                  'v_max_range',
                  'v_min_range',
                  'w_max_range',
                  'w_min_range',
                  'z_push_pos',
                  'z_jump_lim',
                  'x_sheet_offset',
                  'y_sheet_offset']


class AddToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name', 'diameter']
