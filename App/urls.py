from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('past-meetings/', views.PastMeet, name="PastMeet"),
    
]
