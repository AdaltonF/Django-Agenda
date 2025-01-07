from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Login inválido! Tente novamente.")
            return redirect('/login/')
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Event.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        title = request.POST.get('title')
        date = request.POST.get('date').format('YYYY/MM/DD')
        description = request.POST.get('description')
        user = request.user
        id = request.POST.get('id')
        if id:
            Event.objects.filter(id=id).update(title=title,
                                               date=date,
                                               description=description)
        else:
            Event.objects.create(title=title,
                                 date=date,
                                 description=description,
                                 user=user)
    return redirect('/')
@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    user = request.user
    evento = Event.objects.get(id=id_evento)
    if evento.user == user:
        evento.delete()
    return redirect('/')