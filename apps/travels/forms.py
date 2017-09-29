from django import forms
from datetime import date
from ..logreg.models import User
from .models import Plan
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class PlanForm(forms.Form):
    dest = forms.CharField(label="Destination:", max_length=255, min_length=2)
    descr = forms.CharField(label="Description:", max_length=255, min_length=2)
    start = forms.DateField(label="Travel Date From:")
    end = forms.DateField(label="Travel Date To:")
    # start = forms.DateField(label="Travel Date From:", widget=forms.SelectDateWidget(attrs={'type': 'date'}))
    # end = forms.DateField(label="Travel Date To:", widget=forms.SelectDateWidget(attrs={'type': 'date'}))
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/travels/add'
    helper.add_input(Submit('submit', 'Add'))
    def clean(self):
        form_data = self.cleaned_data
        start_date = form_data.get('start')
        if start_date > form_data.get('end'):
            msg = 'Start date must precede end date'
            self.add_error('start', msg)
            self.add_error('end', msg)
        if start_date <= date.today():
            msg = 'Start date must be in the future'
            self.add_error('start', msg)
        return form_data
