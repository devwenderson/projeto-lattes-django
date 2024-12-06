from django.db import models

"""
fazer um model pra cada? 

* fazer instituicao um model só e salvar dados em cookies ate chegar no form de missao

Campos:
    Identificação:
    - CNPJ
    - Nome da instituicao
    - Sigla da instituicao
    - Tipo de estabelecimento
    - Razão social  
    - País
    - Idioma

    Situação cadastral:
    - Informe  a situação 
    - Data da situação cadastral
    - Motivo

    Situação especial:
    - Informe a situação 
    - Data da situação especial

    Informações especiais:
    - Optante pelo o simples
    - Data de início
    - Data de fim
    - optante pelo MEI

    Sócios:
    - Tipo de sócio
    - CPF
    - Nome
    - Qualificação 
    - Data de inclusão na Sociedade

    Representante legal:
    - CPF
    - nome 
    - qualificação

    Endereço:
    - CEP
    - Tipo de CEP
    - Endereço
    - Complemento
    - Bairro    
    - UF/Cidade

    Contato:
    - DDD
    - Telefone 1
    - Ramal
    - Telefone 2
    - Ramal
    - Fax  
    - E-mail institucional
    - Website

    Classificação:
    - Natureza jurídica
    - Categoria administrativa
    - Porte da instituição
    - Setor de atividade econômica
    - Capital Social
    
    Histórico
    - Data da Fundação
    - Informe o histórico:
"""

class Instituicao(models.Model):
    # Identificação
    cnpj = models.CharField(max_length=18, unique=True)
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=50, blank=True, null=True)
    tipo_estabelecimento = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=255)
    pais = models.CharField(max_length=100)
    idioma = models.CharField(max_length=50)

    # Situação cadastral
    situacao_cadastral = models.CharField(max_length=100)
    data_situacao_cadastral = models.DateField()
    motivo_situacao_cadastral = models.TextField(blank=True, null=True)

    # Situação especial
    situacao_especial = models.CharField(max_length=100, blank=True, null=True)
    data_situacao_especial = models.DateField(blank=True, null=True)

    # Informações especiais
    optante_simples = models.BooleanField()
    data_inicio_simples = models.DateField(blank=True, null=True)
    data_fim_simples = models.DateField(blank=True, null=True)
    optante_mei = models.BooleanField()

    # Classificação
    natureza_juridica = models.CharField(max_length=100)
    categoria_administrativa = models.CharField(max_length=100)
    porte = models.CharField(max_length=50)
    setor_atividade = models.CharField(max_length=100)
    capital_social = models.DecimalField(max_digits=15, decimal_places=2)

    # Histórico
    data_fundacao = models.DateField()
    historico = models.TextField(blank=True, null=True)

    # Contato
    ddd = models.CharField(max_length=2)
    telefone1 = models.CharField(max_length=15, blank=True, null=True)
    ramal1 = models.CharField(max_length=10, blank=True, null=True)
    telefone2 = models.CharField(max_length=15, blank=True, null=True)
    ramal2 = models.CharField(max_length=10, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    # Endereço
    cep = models.CharField(max_length=10)
    tipo_cep = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=255)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)

    # Sócios e Representante Legal como campos textuais
    socios = models.TextField(blank=True, null=True, help_text="Informe os sócios separados por vírgula ou de outra forma estruturada.")
    representante_legal = models.CharField(max_length=255, blank=True, null=True, help_text="Nome do representante legal.")

    def __str__(self):
        return self.nome

