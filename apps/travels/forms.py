from django import forms
from ..logreg.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class PlanForm(forms.Form):
    dest = forms.CharField(label="Destination:", max_length=255, min_length=2)
    descr = forms.CharField(label="Description:", max_length=255, min_length=2)
    start = forms.DateField(label="Travel Date From:", widget=forms.SelectDateWidget())
    end = forms.DateField(label="Travel Date To:", widget=forms.SelectDateWidget())
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/travels/add'
    helper.add_input(Submit('submit', 'Register'))
