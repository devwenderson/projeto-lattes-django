from django.shortcuts import render
from instituicao.models import Instituicao

def index(request):
    return render(request, 'index.html')

def cadi_index(request):
    return render(request, 'instituicao/cadi-index.html')

def buscar_instituicao(request):
    context = {}
    if request.method == 'POST':
        tipo_busca = request.POST['tipoBusca']
        if tipo_busca == 'nome':
            nome = request.POST['instituicaoIdentificador']
            instituicoes = Instituicao.objects.all().filter(nome__contains=nome)
            context['instituicoes'] = instituicoes
            
        elif tipo_busca == 'cnpj':
            cnpj = request.POST['instituicaoIdentificador']
            instituicoes = Instituicao.objects.all().filter(cnpj__contains=cnpj)
            context['instituicoes'] = instituicoes

    return render(request,'instituicao/list.html', context)

def cadastro_instituicao(request):
    return render(request, 'instituicao/cadastro')
    