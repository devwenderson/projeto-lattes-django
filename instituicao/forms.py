from django import forms
from .models import Instituicao

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = [
            # Identificação
            'cnpj', 'nome', 'sigla', 'tipo_estabelecimento', 'razao_social',
            'pais', 'idioma',

            # Situação cadastral
            'situacao_cadastral', 'data_situacao_cadastral', 'motivo_situacao_cadastral',

            # Situação especial
            'situacao_especial', 'data_situacao_especial',

            # Informações especiais
            'optante_simples', 'data_inicio_simples', 'data_fim_simples', 'optante_mei',

            # Classificação
            'natureza_juridica', 'categoria_administrativa', 'porte', 'setor_atividade', 'capital_social',

            # Histórico
            'data_fundacao', 'historico',

            # Contato
            'ddd', 'telefone1', 'ramal1', 'telefone2', 'ramal2', 'fax', 'email', 'website',

            # Endereço
            'cep', 'tipo_cep', 'endereco', 'complemento', 'bairro', 'uf', 'cidade',

            # Sócios e Representante Legal
            'socios', 'representante_legal',
        ]

    # Customizando campos para exibição no template
    situacao_especial = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Situação Especial'}))
    data_situacao_especial = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'Data Situação Especial'}))
    # Outros campos podem ser configurados de forma similar conforme a necessidade
