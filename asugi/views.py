from django.shortcuts import render
from asugi.forms import PersonaForm
from .models import Persona

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            tessera = form.cleaned_data['tessera']

        persone = Persona.objects.all()
        print(persone)
        for x in persone:
            if tessera == x.tessera:
                global persona
                persona = x
                return render(request, 'postLogin.html', {'persona' : persona})
        return render(request, 'loginError.html')

def questionario(request):
    if request.method == 'POST':
        return render(request, 'questionario.html', {'persona' : persona})

def compilazione(request):
    setattr(persona, 'questionario', True)
    return render(request, 'postLogin.html', {'persona' : persona})