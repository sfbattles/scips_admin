from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="agent-home"),
    path('about/', views.about, name="agent-about"),
]