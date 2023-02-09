from django.db import models
from colorfield.fields import ColorField


class Continente(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)


class Pais(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    continente = models.ForeignKey('Continente', on_delete=models.DO_NOTHING)


class Marca(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    pais_origem = models.ForeignKey('Pais', on_delete=models.DO_NOTHING, null=True)
    status = models.BooleanField(default=True)


class Carro(models.Model):
    marca = models.ForeignKey('Marca', on_delete=models.DO_NOTHING)
    modelo = models.CharField(max_length=100, null=True)
    ano = models.IntegerField(null=True)
    versao = models.CharField(max_length=50, null=True)
    motor = models.CharField(max_length=200, null=True)
    cambio = models.CharField(max_length=100, null=True)
    comprimento = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    largura = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    altura = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    entre_eixos = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    peso = models.IntegerField(null=True)
    preco = models.DecimalField(max_digits=30, decimal_places=2, null=True)
    status = models.BooleanField(default=True)
    cor_fundo = ColorField(null=True)
    cor_botao = ColorField(null=True)
    cor_specs = ColorField(null=True)
    path = models.FileField(upload_to='cars_img', null=True)
    nm_descritivo = models.CharField(max_length=200, null=True)


class CarrosPendentes(models.Model):
    marca = models.ForeignKey('Marca', on_delete=models.DO_NOTHING)
    modelo = models.CharField(max_length=100, null=True)
    ano = models.IntegerField(null=True)
