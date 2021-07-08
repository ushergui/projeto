from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^cadastrar_estado', cadastrar_estado, name='cadastrar_estado'),

]