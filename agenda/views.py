from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContatoForm
import json
from .models import Contato


def index(request):
    form = ContatoForm()
    return render(request, 'agenda/index.html', {'form': form})


def listar_json(request):
    contatos = Contato.objects.all()

    json.dumps(contatos)
    return HttpResponse(contatos, content_type='application/json')

def novo(request):
    contato = Contato(nome=request.POST['nome'], email=request.POST['email'], telefone=request.POST['telefone'])
    contato.save()

    return HttpResponse()
