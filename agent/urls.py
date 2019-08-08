from django.conf import settings
from django.urls import path,include
from . import views
from .views import (
    AgentListView,
    AgentDetailView,
    AgentCreateView,
    AgentUpdateView,
    AgentDeleteView,
    MasterAgentDetailView
)


urlpatterns = [
    # class base view need be converted into a view in order to be displayed.
    # running .as_view() 
    path('', AgentListView.as_view(), name="agent-home"),
    path('master_agent/<int:pk>/', MasterAgentDetailView.as_view(), name='master-agent'),
    path('agent/<int:id>/', AgentDetailView.as_view(), name="agent-detail"),
    path('agent/new/', AgentCreateView.as_view(), name="agent-create"),
    path('agent/<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update'),
    path('agent/<int:pk>/delete/', AgentDeleteView.as_view(), name='agent-delete'),    
    path('home/', views.new_agent, name="agent-new-agent"),
    path('about/', views.about, name="agent-about"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns