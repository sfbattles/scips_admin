from django.db import models
from django.urls import reverse

class PhoneType(models.Model):
    type = models.CharField(max_length=200)

    class Meta:
        verbose_name = "PhoneType"
        verbose_name_plural = "PhoneTypes"
        db_table = 'PhoneType'

    def __str__(self):
        return str(self.type)
    

class AgentMaster(models.Model):
    master_code = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "AgentMaster"
        verbose_name_plural = "AgentMasters"
        db_table = 'AgentMaster'

    def __str__(self):
        #return str(self.master_code)
        return str(self.id) # updated so the query will return the ID and send it in url 


class Agent(models.Model):
    agent_no = models.PositiveIntegerField(unique=True)
    agent_master_code = models.ForeignKey(AgentMaster, on_delete=models.CASCADE,related_name='subagents')
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=9)
    status = models.PositiveSmallIntegerField()
    
    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agencies"
        db_table = 'Agent'

    def __str__(self):
        return str(self.agent_no)

#this is used to tell django where to go after it creates a agent
#reverse will tells where to go to find the knewly created URL
#kwargs={'pk':self.pk} find the created agent 
#agent-detail is the route to go to to see the newly created instance
    def get_absolute_url(self):
        return reverse('agent-detail',kwargs={'pk':self.pk})


class AgentAddress(models.Model):
    agent_no = models.ForeignKey(Agent, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=9)

    class Meta:
        verbose_name = "AgentAddress"
        verbose_name_plural = "AgentAddresses"
        db_table = 'AgentAddress'

    def __str__(self):
        return str(self.agent_no)

class AgentPhone(models.Model):
    agent_no = models.ForeignKey(Agent, on_delete=models.CASCADE)
    phone    = models.CharField(max_length=11,null=True,blank=True)
    phone_extension = models.CharField(max_length=20,null=True,blank=True)
    phone_type = models.ForeignKey(PhoneType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "AgentPhone"
        verbose_name_plural = "AgentPhones"
        db_table = 'AgentPhone'

    def __str__(self):
        return str(self.agent_no)
        

class AgentEmail(models.Model):
    agent_no = models.ForeignKey(Agent, on_delete=models.CASCADE)
    email = models.EmailField()
    get_portal_email = models.BooleanField(default=True)

    class Meta:
        verbose_name = "AgentEmail"
        verbose_name_plural = "AgentEmails"
        db_table = 'AgentEmail'

    def __str__(self):
        return str(self.email)

class State(models.Model):
    state_abbreviation = models.CharField(max_length = 2)
    state = models.CharField(max_length=50)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        db_table = 'State'

    def __str__(self):
        return str(self.state)