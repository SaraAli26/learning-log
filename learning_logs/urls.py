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
    #Display the seperate entries for each topic
    path('topics/<int:topic_id>/', views.topic, name="topic"),
    # Add the urls for the forms for users other than admin to insert data_added
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry for a spesfic topic
    path('new_entry/<int:topic_id>', views.new_entry, name="new_entry"),
    # edit each entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name="edit_entry"),

]
