from django.db import models


# Create your models here.

class Estado(models.Model):
    nome_estado = models.CharField(max_length=20, null=False)
    abreviatura_estado = models.CharField(max_length=2, null = False)

    def __str__(self):
        return self.nome_estado
