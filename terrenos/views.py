from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

class estado_form(ModelForm):
    class Meta:
        model = Estado
        fields = ['nome_estado', 'abreviatura_estado']

def cadastrar_estado(request, template_name='estado/estado_form.html'):
    form = estado_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_estado')
    return render(request, template_name, {'form': form})