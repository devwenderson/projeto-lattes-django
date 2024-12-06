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
            instituicao = Instituicao.objects.filter(nome__contains=nome)
            context['instituicao'] = instituicao
        elif tipo_busca == 'cnpj':
            cnpj = request.POST['instituicaoIdentificador']
            instituicao = Instituicao.objects.filter(cnpj__contains=cnpj)
            context['instituicao'] = instituicao
    return render(request,'instituicao/list.html', context)

def cadastro_instituicao(request):
    return render(request, 'instituicao/cadastro')
    