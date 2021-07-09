from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^cadastrar_estado', cadastrar_estado, name='cadastrar_estado'),
    url(r'^listar_estado', listar_estado, name='listar_estado'),
    url(r'^excluir_estado/(?P<pk>[0-9]+)', excluir_estado, name='excluir_estado'),
    url(r'^editar_estado/(?P<pk>[0-9]+)', editar_estado, name='editar_estado'),
    url(r'^cadastrar_cidade', cadastrar_cidade, name='cadastrar_cidade'),
    url(r'^listar_cidade', listar_cidade, name='listar_cidade'),
    url(r'^excluir_cidade/(?P<pk>[0-9]+)', excluir_cidade, name='excluir_cidade'),
    url(r'^editar_cidade/(?P<pk>[0-9]+)', editar_cidade, name='editar_cidade'),

]