from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from learning_logs.models import Topic, Entry
from .forms import TopicForm

# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

def base(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/base.html')

def topics(request):
    """Display topics"""
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Dispaly the Entries for each topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.all()
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

#method for forms for data to be entered by user
def new_topic(request):
    """Add a new topic by users other than admin."""
    if request.method != 'POST':
        # Condition check if there is data submitted or not, if not then create an empty form
        form = TopicForm()
    else:
        # If request is post then save data to DB
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs/topics.html'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
