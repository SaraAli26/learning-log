"""Defines URL patterm for learning_logs whic is the app"""

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #Home page
    path('', views.index, name="index"),
    path('base/', views.base, name="base"),
    #Dispaly all topics
    path('topics/', views.topics, name="topics"),
]
