from django.contrib import admin
from agent.models import Agent
from agent.models import PhoneType
from agent.models import AgentPhone
from agent.models import AgentMaster
from .models import AgentEmail

# Register your models here.
admin.site.register(Agent)
admin.site.register(PhoneType)
admin.site.register(AgentPhone)
admin.site.register(AgentMaster)
admin.site.register(AgentEmail)