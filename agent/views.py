from django.shortcuts import render, get_object_or_404
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
from .models import Agent
from .models import AgentMaster

@login_required
def home(request):
    context = {
        'agents': Agent.objects.all() 
    }
    # print(context)
    return render(request,'agent/agent.html', context)

def main(request):
    return render(request,'agent/main.html')

# @method_decorator(login_required, name='dispatch')
class AgentListView(LoginRequiredMixin, ListView):
    model = Agent
    template_name = 'agent/agent.html'  #<app>/<model>_viewtype.html agent/agent_list.html by default
    context_object_name = 'agents'
    ordering = ['name']  
    paginate_by = 4

class MasterAgentDetailView(LoginRequiredMixin, DetailView):
    model = Agent
    template_name = 'agent/master_agent.html'  #<app>/<model>_viewtype.html agent/agent_list.html by default
    context_object_name = 'agent' 
    pk_url_kwarg = 'agent_master_code'

    def get_queryset(self):
        print(f'this is self {self}')
        print(f'pk_url_kwarg {pk_url_kwarg}')
        master_agent = get_object_or_404(Agent,id = self.kwargs.get('agent_master_code')) # gets an object
        return Agent.objects.filter(agent_master_code__master_code = master_agent.id)

# @method_decorator(login_required, name='dispatch')
class AgentDetailView(LoginRequiredMixin,DetailView):
    model = Agent 
 
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
