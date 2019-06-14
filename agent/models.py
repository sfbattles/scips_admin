from django.db import models
from phone_field import PhoneField

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
        return str(self.master_code)


class Agent(models.Model):
    agent_no = models.PositiveIntegerField(unique=True)
    agent_master_code = models.ForeignKey(AgentMaster, on_delete=models.CASCADE)
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

class AgentPhone(models.Model):
    agent_no = models.ForeignKey(Agent, on_delete=models.CASCADE)
    phone    = models.CharField(max_length=11)
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

    class Meta:
        verbose_name = "AgentEmail"
        verbose_name_plural = "AgentMails"
        db_table = 'AgentEmail'

    def __str__(self):
        return str(self.email)