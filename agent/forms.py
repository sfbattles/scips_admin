#from django.forms import ModelForm
from django import forms
from django.forms import ModelChoiceField
from agent.models import Agent, AgentPhone, AgentEmail, PhoneType, AgentMaster, State
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

class StateModelChoiceField(ModelChoiceField):  #overrid the __str__ return with what you have below
    def label_from_instance(self, obj):
        return "%s" % (obj.state_abbreviation)


class AgentModelChoiceField(ModelChoiceField):  #overrid the __str__ return with what you have below
    def label_from_instance(self, obj):
        return "%s %s" % (obj.master_code,obj.name)


class AgentMasterForm(forms.Form):
    master_code = forms.ChoiceField(widget=forms.Select())
    state = StateModelChoiceField(queryset=State.objects.all(),to_field_name="id")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['master_code'].choices=[(master_code.id,master_code.name) for master_code in AgentMaster.objects.exclude(master_code__gt=9000).order_by('name') ]
        self.fields['state'].choices=[(state.id,state.state_abbreviation) for state in State.objects.all().order_by('state_abbreviation')]


class AgentForm(forms.ModelForm):
    agent_master_code = AgentModelChoiceField(queryset=AgentMaster.objects.all(),to_field_name="id")
    class Meta:
        model = Agent
        fields = ['agent_no','agent_master_code','name','address','city','state','zipcode']
        widgets = {
            'agent_no' : forms.TextInput(
            attrs={'placeholder': 'Enter Agent Number'})
        }
    name = forms.CharField(widget=forms.TextInput())
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    city = forms.CharField()
    state = StateModelChoiceField(queryset=State.objects.all(),to_field_name="id")
    zipcode = forms.CharField(label='Zip')


# class CrispyAgentForm(AgentForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('agent_no', css_class='form-group col-md-6 mb-0'),
#                 Column('agent_master_code', css_class='form-group col-md-6 mb-0'),
#                 Column('name', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             'address',
#             Row(
#                 Column('city', css_class='form-group col-md-6 mb-0'),
#                 Column('state', css_class='form-group col-md-4 mb-0'),
#                 Column('zipcode', css_class='form-group col-md-2 mb-0'),
#                 css_class='form-row'
#             ),
#             Submit('submit', 'Add Agent')
#         )


class AgentEmailForm(forms.ModelForm):
    class Meta:
        model = AgentEmail
        fields = ('email','get_portal_email')
        
        
class AgentPhoneForm(forms.ModelForm):
    phone = forms.CharField(label='Your Phone')
    class Meta:
        model = AgentPhone
        fields = ('phone','phone_extension','phone_type')  
