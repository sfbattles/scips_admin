from django.forms import ModelForm
from django import forms
from agent.models import Agent, AgentPhone, AgentEmail, PhoneType, AgentMaster

# class AgentMasterForm(ModelForm):
#     class Meta:
#         model = AgentMaster
#         # fields = ('__all__',)
#         fields = ('master_code',)

class AgentMasterForm(forms.Form):
    master_code = forms.ChoiceField(widget=forms.Select(attrs={'master_code' : 'form_control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['master_code'].choices=[(master_code.id,master_code.name) for master_code in AgentMaster.objects.exclude(master_code__gt=9000) ]

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        # fields = ('__all__',)
        fields = ('agent_no',
              'name',
              'address',
              'city',
              'state',
              'zipcode',
              'status',)


class AgentEmailForm(ModelForm):
    class Meta:
        model = AgentEmail
        fields = ('email','get_portal_email')
        
        
class AgentPhoneForm(ModelForm):
    class Meta:
        model = AgentPhone
        fields = ('phone','phone_extension','phone_type')
        