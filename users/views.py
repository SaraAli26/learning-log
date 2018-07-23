
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """Logout the user"""
    logout(request)
    return redirect('index')



def register(request):
    """Register a new user."""
    if request.method != 'POST':
        #Dispaly the blank registration form
        form = UserCreationForm()
    else:
        #Handle the newly created user when he/she signup
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Login the user and redirect to home page right after
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'users/register.html', context)
