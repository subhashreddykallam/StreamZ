from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index_view(request):
    return render(request, 'index.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login_url')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html',context)

def login_view(request):
    return render(request, 'registration/login.html')


