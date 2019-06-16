from django.urls import path
from . import views
from .views import (
    AgentListView,
    AgentDetailView,
    AgentCreateView,
    AgentUpdateView,
    AgentDeleteView,
)

urlpatterns = [
    # class base view need be converted into a view in order to be displayed.
    # running .as_view() 
    path('', AgentListView.as_view(), name="agent-home"),
    path('agent/<int:pk>/', AgentDetailView.as_view(), name="agent-detail"),
    path('agent/<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update'),
    path('agent/<int:pk>/delete/', AgentDeleteView.as_view(), name='agent-delete'),
    path('agent/new/', AgentCreateView.as_view(), name="agent-create"),
    path('about/', views.about, name="agent-about"),
]