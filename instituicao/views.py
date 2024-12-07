from django.shortcuts import render
from instituicao.models import Instituicao

def index(request):
    return render(request, 'index.html')

def cadi_index(request):
    return render(request, 'instituicao/cadi-index.html')

def buscar_instituicao(request):
    context = {}
    template_name = 'instituicao/list.html'
    if request.method == 'POST':
        tipo_busca = request.POST['tipoBusca']
        if tipo_busca == 'nome':
            nome = request.POST['instituicaoIdentificador']
            instituicoes = Instituicao.objects.all().filter(nome__contains=nome)
            context['instituicoes'] = instituicoes
            template_name = 'instituicao/list.html'
            if len(instituicoes) == 0:
                template_name = 'instituicao/instituicao-nao-encontrada.html'
            
        elif tipo_busca == 'cnpj':
            cnpj = request.POST['instituicaoIdentificador']
            instituicoes = Instituicao.objects.all().filter(cnpj__contains=cnpj)
            context['instituicoes'] = instituicoes
            if len(instituicoes) == 0:
                template_name = 'instituicao/instituicao-nao-encontrada.html'
    return render(request,template_name, context)

def cadastro_instituicao(request):
    return render(request, 'instituicao/create.html')
    