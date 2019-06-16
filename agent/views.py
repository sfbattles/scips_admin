from django.shortcuts import render
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
