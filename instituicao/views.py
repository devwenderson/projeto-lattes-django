from django.shortcuts import render
from django.http import JsonResponse
from .forms import InstituicaoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cadi_index(request):
    return render(request, 'instituicao/cadi-index.html')

def cadastro_instituicao(request):
    return render(request, 'instituicao/cadastro')
    