from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Agent

@login_required
def home(request):
    context = {
        'agents': Agent.objects.all() 
    }
    print(context)
    return render(request,'agent/agent.html', context)

@login_required
def about(request):
    return render(request,'agent/about.html')
