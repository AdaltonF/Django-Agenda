from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from core.models import Event

# Create your views here.
def login_user(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def listar_eventos(request):
    active_user = request.user
    event = Event.objects.filter(user=active_user).order_by('-date')
    data = {'events': event}
    return render(request, 'agenda.html', data)


def submit_login(request):
    if request.POST:
        print(request.build_absolute_uri())
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        return redirect('/')