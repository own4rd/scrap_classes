from django.db import models

class Advogado(models.Model):
    nome = models.CharField(max_length=100)

class Parte(models.Model):
    nome = models.CharField(max_length=100)

class Processo(models.Model):
    numero = models.CharField(max_length=30)
    vara = models.CharField(max_length=100)
    comarca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    data_recebimento = models.DateField()
    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE)