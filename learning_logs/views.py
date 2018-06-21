from django.shortcuts import render

from learning_logs.models import Topic
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
