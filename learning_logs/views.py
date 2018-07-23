from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from learning_logs.models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')


@login_required
def base(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/base.html')


@login_required
def topics(request):
    """Display topics"""
    #line changed to ristrect objects to the only aythorised user, the owner of it
    topics = Topic.objects.filter(owner=request.user).order_by('date_published')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Dispaly the Entries for each topic"""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    check_topic_owner(topic.owner, request.user)
    entries = topic.entry_set.all()
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic by users other than admin."""
    if request.method != 'POST':
        # Condition check if there is data submitted or not, if not then create an empty form
        form = TopicForm()
    else:
        # If request is post then save data to DB
        form = TopicForm(request.POST)
        if form.is_valid():
            #associate every new topic with its user
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('topics')
            #return HttpResponseRedirect(reverse('learning_logs/topics')) Note: But why it was not working
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """ Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #No data submitted; process data
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('topics')

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic.owner, request.user)
    if request.method != 'POST':
        # prefill form with the old values
        form = EntryForm(instance=entry)

    else:
        # save new edited data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics')

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def check_topic_owner(topic_owner, request_user):
    """Method for cheking that the topic is matching to th ecurrently logged in user"""
    if topic_owner != request_user:
        raise Http404
