from django.shortcuts import render
from core.models import Event


# Create your views here.
def listar_eventos(request):
    active_user = request.user
    event = Event.objects.filter(user=active_user).order_by('-date')
    data = {'events': event}
    return render(request, 'agenda.html', data)
