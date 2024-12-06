# Generated by Django 5.1.3 on 2024-12-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo_estabelecimento', models.CharField(choices=[('Matriz', 'Matriz'), ('Filial', 'Filial')], max_length=100)),
                ('razao_social', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=100)),
                ('idioma', models.CharField(max_length=50)),
                ('situacao_cadastral', models.CharField(choices=[('Nula', 'Nula'), ('Ativa', 'Ativa'), ('Suspensa', 'Suspensa'), ('Inapta', 'Inapta'), ('Baixada', 'Baixada')], max_length=100)),
                ('data_situacao_cadastral', models.DateField()),
                ('motivo_situacao_cadastral', models.TextField(blank=True, null=True)),
                ('situacao_especial', models.CharField(blank=True, max_length=100, null=True)),
                ('data_situacao_especial', models.DateField(blank=True, null=True)),
                ('optante_simples', models.BooleanField()),
                ('data_inicio_simples', models.DateField(blank=True, null=True)),
                ('data_fim_simples', models.DateField(blank=True, null=True)),
                ('optante_mei', models.BooleanField()),
                ('tipo_socio', models.CharField(choices=[('Pessoa jurídica', 'Pessoa jurídica'), ('Pessoa física', 'Pessoa física'), ('Sócio estrangeiro', 'Sócio estrangeiro')], max_length=80, verbose_name='Tipo de sócio')),
                ('nome_socio', models.CharField(max_length=70, verbose_name='Nome do sócio')),
                ('cpf_socio', models.CharField(max_length=14, verbose_name='CPF do sócio')),
                ('qualificacao_socio', models.CharField(choices=[('Presidente', 'Presidente'), ('Diretor', 'Diretor'), ('Vice-presidente', 'Vice-presidente')], max_length=70, verbose_name='Qualificação do sócio')),
                ('data_inclusao_socioedade', models.DateField(verbose_name='Data de Inclusão na Sociedade')),
                ('nome_representante', models.CharField(max_length=60, verbose_name='Nome do representante legal')),
                ('cpf_representante', models.CharField(max_length=14, verbose_name='CPF do representante legal')),
                ('qualificacao_representante', models.CharField(choices=[('Administrador', 'Administrador'), ('Curador', 'Curador'), ('Mãe', 'Mãe'), ('Pai', 'Pai'), ('Tutor', 'Tutor'), ('Procurador', 'Procurador')], max_length=70, verbose_name='Qualificação do representante legal')),
                ('cep', models.CharField(max_length=10)),
                ('tipo_cep', models.CharField(blank=True, max_length=50, null=True)),
                ('endereco', models.CharField(max_length=255)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=100)),
                ('ddd', models.CharField(max_length=2)),
                ('telefone1', models.CharField(blank=True, max_length=15, null=True)),
                ('ramal1', models.CharField(blank=True, max_length=10, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=15, null=True)),
                ('ramal2', models.CharField(blank=True, max_length=10, null=True)),
                ('fax', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('natureza_juridica', models.CharField(max_length=100)),
                ('categoria_administrativa', models.CharField(max_length=100)),
                ('porte', models.CharField(max_length=50)),
                ('setor_atividade', models.CharField(max_length=100)),
                ('capital_social', models.DecimalField(decimal_places=2, max_digits=15)),
                ('data_fundacao', models.DateField()),
                ('historico', models.TextField(blank=True, null=True)),
                ('missao', models.TextField(verbose_name='Missão da instituição')),
            ],
            options={
                'verbose_name': 'Instituição',
                'verbose_name_plural': 'Instituições',
            },
        ),
    ]
