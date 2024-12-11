from django.shortcuts import render
from instituicao.models import Instituicao
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html')

def cadi_index(request):
    return render(request, 'instituicao/cadi-index.html')

def detalhar_instituicao(request, pk):
    context = {}
    context['instituicao'] = Instituicao.objects.get(pk=pk)
    return render(request, 'instituicao/detail.html', context)


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
    if (request.method == 'POST'):
        # Identificação
        nome = request.POST['nome']
        cnpj = request.POST['cnpj']
        sigla = request.POST['sigla']
        tipo_estabelecimento = request.POST['tipo_estabelecimento']
        razao_social = request.POST['razao_social']
        pais = request.POST['pais']
        idioma = request.POST['idioma']
        
        # Situação cadastral
        situacao_cadastral = request.POST['situacao_cadastral']
        data_situacao_cadastral = request.POST['data_situacao_cadastral']
        motivo = request.POST['motivo']
        
        # Situação especial
        situacao_especial = request.POST['situacao_especial']
        data_situacao_especial = request.POST['data_situacao_especial']
        
        # Informações especiais
        optante_simples = request.POST['optante_simples']
        data_inicio_simples = request.POST['data_inicio_simples']
        data_fim_simples = request.POST['data_fim_simples']
        mei = request.POST['mei']
        
        # Sócios e Representante Legal como campos textuais
        tipo_socio = request.POST['tipo_socio']
        cpf_socio = request.POST['cpf_socio']
        nome_socio = request.POST['nome_socio']
        qualificacao_socio = request.POST['qualificacao_socio']
        data_inclusao_sociedade = request.POST['data_inclusao_sociedade']
        cpf_representante = request.POST['cpf_representante']
        nome_representante = request.POST['nome_representante']
        qualificacao_representante = request.POST['qualificacao_representante']
        
        # Endereço
        endereco = request.POST['endereco']
        cep = request.POST['cep']
        uf = request.POST['uf']
        cidade = request.POST['cidade']
        numero_caixa_postal = request.POST['numero_caixa_postal']
        
        # Contato
        telefone1 = request.POST['telefone1']
        telefone2 = request.POST['telefone2']
        fax = request.POST['fax']
        email = request.POST['email']
        website = request.POST['website']
        
        # Classificação
        natureza_juridica = request.POST['natureza_juridica']
        categoria_administrativa = request.POST['categoria_administrativa']
        porte = request.POST['porte']
        setor_atividade = request.POST['setor_atividade']
        capital_social = request.POST['capital_social']
        
        # Histórico
        data_fundacao = request.POST['data_fundacao']
        historico = request.POST['historico']
        
        # Missão
        missao = request.POST['missao']
        
        instituicao = Instituicao.objects.create(
            cnpj=cnpj,
            nome=nome,
            sigla=sigla,
            tipo_estabelecimento=tipo_estabelecimento,
            razao_social=razao_social,
            pais=pais,
            idioma=idioma,
            situacao_cadastral=situacao_cadastral,
            data_situacao_cadastral=data_situacao_cadastral,
            motivo_situacao_cadastral=motivo,
            situacao_especial=situacao_especial,
            data_situacao_especial=data_situacao_especial,
            optante_simples=optante_simples,
            data_inicio_simples=data_inicio_simples,
            data_fim_simples=data_fim_simples,
            optante_mei=mei,
            tipo_socio=tipo_socio,
            cpf_socio=cpf_socio,
            nome_socio=nome_socio,
            qualificacao_socio=qualificacao_socio,
            data_inclusao_sociedade=data_inclusao_sociedade,
            cpf_representante=cpf_representante,
            nome_representante=nome_representante,
            qualificacao_representante=qualificacao_representante,
            endereco=endereco,
            cep=cep,
            uf=uf,
            cidade=cidade,
            numero_caixa_postal=numero_caixa_postal,
            telefone1=telefone1,
            telefone2=telefone2,
            fax=fax,
            email=email,
            website=website,
            natureza_juridica=natureza_juridica,
            categoria_administrativa=categoria_administrativa,
            porte=porte,
            setor_atividade=setor_atividade,
            capital_social=capital_social,
            data_fundacao=data_fundacao,
            historico=historico,
            missao=missao
        )
        instituicao.save()
        reverse_lazy('buscar-instituicao')
    return render(request, 'instituicao/create.html')
