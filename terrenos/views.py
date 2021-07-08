from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

class formulario_estado(ModelForm):
    class Meta:
        model = Estado
        fields = ['nome_estado', 'abreviatura_estado']

def cadastrar_estado(request, template_name='estado/formulario_estado.html'):
    form = formulario_estado(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_estado')
    return render(request, template_name, {'form': form})

def listar_estado(request, template_name='estado/listar_estado.html'):
    estado = Estado.objects.all()
    estados = {'lista': estado}
    return render(request, template_name, estados)

def excluir_estado(request, pk):
    estado = Estado.objects.get(pk=pk)
    if request.method == "POST":
        estado.delete()
        return redirect('listar_estado')
    return render(request, 'estado/excluir_estado.html', {'estado': estado})

def editar_estado(request, pk, template_name='estado/formulario_estado.html'):
    estado = get_object_or_404(Estado, pk=pk)
    if request.method == "POST":
        form = formulario_estado(request.POST, instance=estado)
        if form.is_valid():
            estado = form.save()
            return redirect('listar_estado')
    else:
        form = formulario_estado(instance=estado)
    return render(request, template_name, {'form': form})
