from django.db import models


# Create your models here.

class Estado(models.Model):
    nome_estado = models.CharField(max_length=20, null=False)
    abreviatura_estado = models.CharField(max_length=2, null = False)

    def __str__(self):
        return self.nome_estado

class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=40, null=False)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_cidade