from django.urls import path 
from instituicao.views import index, cadi_index, buscar_instituicao,cadastro_instituicao

urlpatterns = [
    path('', index, name='index'), 
    path('diretorio-de-instituicoes/', cadi_index, name='cadi-index'),
    path('instituicao/buscar/', buscar_instituicao, name='buscar-instituicao'),
    path('instituicao/cadastro/', cadastro_instituicao, name='cadastro-instituicao'),
]