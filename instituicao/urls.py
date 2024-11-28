from django.urls import path 
from instituicao.views import index

urlpatterns = [
    path('', index, name='index'), 
]