from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse 
from django.forms import modelformset_factory, inlineformset_factory

from django.template.context_processors import csrf
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                )
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Agent, AgentMaster, AgentEmail, AgentPhone
from .forms import AgentForm, AgentEmailForm, AgentPhoneForm, AgentMasterForm


@login_required
def home(request):
    context = {
        'agents': Agent.objects.all() 
    }
    # print(context)
    return render(request,'agent/agent.html', context)

def main(request):
    return render(request,'agent/new_agent.html')

# @method_decorator(login_required, name='dispatch')
class AgentListView(LoginRequiredMixin, ListView):
    model = Agent
    template_name = 'agent/agent_list.html'  #<app>/<model>_viewtype.html agent/agent_list.html by default
    context_object_name = 'agents'
    ordering = ['name']  
    paginate_by = 4

class MasterAgentDetailView(LoginRequiredMixin, DetailView):
    model = AgentMaster
    template_name = 'agent/master_agent.html'  #<app>/<model>_viewtype.html agent/agent_list.html by default
    context_object_name = 'agentmaster' 

    def get_queryset(self):
        master_agent= get_object_or_404(AgentMaster,id=self.kwargs.get('pk')) # gets an object
        return AgentMaster.objects.filter(id=master_agent.id)

# @method_decorator(login_required, name='dispatch')
class AgentDetailView(LoginRequiredMixin,DetailView):
    model = Agent 

    def get_object(self):  #if you do not pass pk or slug in detail view is will error and you need to
                            #override the get_object(self) function if you pass "id"  it looks in the kwargs to get the ID from the urls.py
                            #path('agent/<int:id>/', AgentDetailView.as_view(), name="agent-detail"),
                            #to get the <int:id> from the url you need to use self.kwargs.get("id")
	    id_ = self.kwargs.get("id")  #kwargs args is how you pass the parameter to the detail view.
	    return get_object_or_404(Agent,id=id_)

# @method_decorator(login_required, name='dispatch')
class AgentCreateView(LoginRequiredMixin,CreateView):
    model = Agent 
    fields = ['agent_no',
              'agent_master_code',
              'name',
              'address',
              'city',
              'state',
              'zipcode',
              'status']

class AgentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Agent 
    fields = ['agent_no',
              'agent_master_code',
              'name',
              'address',
              'city',
              'state',
              'zipcode',
              'status']

    def test_func(self):
        # agent = self.get_object() #get current Agent
        if self.request.user.profile.user_access_id == 3:
            return True
        return False

class AgentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Agent 
    success_url = '/'
    def test_func(self):
        if self.request.user.profile.user_access_id == 3:  #company User
            return True
        return False


@login_required
def about(request):
    return render(request,'agent/about.html')

@login_required
def agentphone(request, agent_id):
    currentagent = Agent.objects.get(pk=agent_id)
    AgentPhoneFormSet = inlineformset_factory(Agent,AgentPhone, fields=('phone','phone_extension','phone_type'), extra=1, labels={'phone':"Phone",'phone_extension':'Extension','phone_type': 'Phone Type'})
    if request.method == 'POST':
        formset = AgentPhoneFormSet(request.POST,instance=currentagent)
        if formset.is_valid():
            formset.save()
            return redirect('agent-phone', agent_id=currentagent.id)
    else:
        formset = AgentPhoneFormSet(instance=currentagent)
    return render(request,'agent/agentphone.html', {'formset' : formset})


@login_required
def new_agent(request):
    if request.method == "POST":
        agent_master_form = AgentMasterForm(request.POST)
        agent_form = AgentForm(request.POST)
        agent_email_form = AgentEmailForm(request.POST)
        agent_phone_form = AgentPhoneForm(request.POST)
        if (agent_form.is_valid() and 
            agent_email_form.is_valid() and 
            agent_phone_form.is_valid() and 
            agent_master_form.is_valid()):                   
            agent_master_code = request.POST.get('master_code',default=None)
            print(f"this is the master code {agent_master_code} ")
            agent_master = AgentMaster.objects.get(pk=agent_master_code)   
            agent = agent_form.save(False)
            agentphone = agent_phone_form.save(False)
            agentemail = agent_email_form.save(False)
            agent.agent_master_code = agent_master
            agent.save()
            agentemail.agent_no = agent
            agentphone.agent_no = agent            
            agentemail.save()
            agentphone.save()                        
            return redirect(reverse('agent-new-agent'))
    else:
        agent_master_form = AgentMasterForm()
        agent_form = AgentForm()  #creates an instance of the agent_form
        agent_email_form = AgentEmailForm()
        agent_phone_form = AgentPhoneForm()

    args = {}
    args.update(csrf(request))
    args['agent_master_form'] = agent_master_form
    args['agent_form'] = agent_form
    args['agent_email_form'] = agent_email_form
    args['agent_phone_form'] = agent_phone_form

    # return render(request, 'agent/new_agent.html', args)
    return render(request, 'agent/agent_address_form.html', args)
