from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Cria o formulário do Estado
class formulario_estado(ModelForm):
    class Meta:
        model = Estado
        fields = ['nome_estado', 'abreviatura_estado']

# Cria a função de cadastrar um estado
def cadastrar_estado(request, template_name='estado/formulario_estado.html'):
    form = formulario_estado(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_estado')
    return render(request, template_name, {'form': form})


# Cria a função de listar os estados
def listar_estado(request, template_name='estado/listar_estado.html'):
    estado = Estado.objects.all()
    estados = {'lista': estado}
    return render(request, template_name, estados)



# Cria a função de deletar um estado
def excluir_estado(request, pk):
    estado = Estado.objects.get(pk=pk)
    if request.method == "POST":
        estado.delete()
        return redirect('listar_estado')
    return render(request, 'estado/excluir_estado.html', {'estado': estado})



# Cria a função de editar um estado
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



# Cria o formulário do Cidade
class formulario_cidade(ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome_cidade', 'estado']



# Cria a função de cadastrar uma cidade
def cadastrar_cidade(request, template_name='cidade/formulario_cidade.html'):
    form = formulario_cidade(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_cidade')
    return render(request, template_name, {'form': form})




# Cria a função de listar as cidades
def listar_cidade(request, template_name='cidade/listar_cidade.html'):
    cidade = Cidade.objects.all()
    cidades = {'lista': cidade}
    return render(request, template_name, cidades)


# Cria a função de deletar uma cidade
def excluir_cidade(request, pk):
    cidade = Cidade.objects.get(pk=pk)
    if request.method == "POST":
        cidade.delete()
        return redirect('listar_cidade')
    return render(request, 'cidade/excluir_cidade.html', {'cidade': cidade})



# Cria a função de editar um cidade
def editar_cidade(request, pk, template_name='cidade/formulario_cidade.html'):
    cidade = get_object_or_404(Cidade, pk=pk)
    if request.method == "POST":
        form = formulario_cidade(request.POST, instance=cidade)
        if form.is_valid():
            cidade = form.save()
            return redirect('listar_cidade')
    else:
        form = formulario_cidade(instance=cidade)
    return render(request, template_name, {'form': form})
