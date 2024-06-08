from django import forms
from django.forms import ModelForm
from PIL import Image
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget = forms.DateInput(format='%d.%m.%Y', attrs={'class': 'form-control', 'placeholder': 'DD.MM.YYYY'})
        self.fields['start_date'].input_formats = ['%d.%m.%Y']

        self.fields['annual_leave_days'].widget.attrs['placeholder'] = ''
        self.fields['free_days'].widget.attrs['placeholder'] = ''
        self.fields['paid_leave_days'].widget.attrs['placeholder'] = ''

        for field in ['annual_leave_days', 'free_days', 'paid_leave_days']:
            value = getattr(self.instance, field)
            if value in [None, 0]:
                self.fields[field].widget.attrs['value'] = ''

        self.fields['contract_type'].required = True
        self.fields['department'].required = True
        self.fields['gender'].required = True

        if self.instance.contract_type == 'permanent':
            self.fields['contract_duration'].required = False



    def clean(self):
        cleaned_data = super().clean()
        contract_type = cleaned_data.get('contract_type')
        contract_duration = cleaned_data.get('contract_duration')

        if contract_type == 'permanent' and contract_duration:
            self.add_error('contract_duration', "Permanent contract doesn't require a contract duration. Please leave this field empty.")

        if contract_type != 'permanent' and not contract_duration:
            self.add_error('contract_duration', "Contract duration is required if the contract is not permanent. Please fill in this field.")

        return cleaned_data