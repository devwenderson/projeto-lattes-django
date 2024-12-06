from django.urls import path 
from instituicao.views import index, cadastro_instituicao, cadi_index

urlpatterns = [
    path('', index, name='index'), 
    path('diretorio-de-instituicoes/', cadi_index, name='cadi-index'),
    path('instituicao/cadastro/', cadastro_instituicao, name='cadastro-instituicao'),
]