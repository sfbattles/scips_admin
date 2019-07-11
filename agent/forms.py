from django.forms import ModelForm
from agent.models import Agent, AgentPhone, AgentEmail, PhoneType, AgentMaster

class AgentMasterForm(ModelForm):
    class Meta:
        model = AgentMaster
        # fields = ('__all__',)
        fields = ('master_code',
                  'name')

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
        