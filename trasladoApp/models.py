from django.db import models
from django.contrib.auth.models import User

class Veiculo(models.Model):
    placa = models.CharField(max_length=20)
    modelo = models.CharField(max_length=10)
    ano =   models.CharField(max_length=4)
    marca = models.CharField(max_length=10)

    def __str__(self):
        return self.placa + " - " + self.marca

class Motorista(models.Model):
    nome = models.CharField(max_length=128)
    cnh = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome + " - " + self.cnh

class Departamento(models.Model):
    nome = models.CharField(max_length=128)
    chefe = models.CharField(max_length=128)

    def __str__(self):
        return self.nome + " - " + self.chefe

class Funcionario(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=14)
    departamento = models.ForeignKey(Departamento, null=True, blank=False)
    usuario = models.ForeignKey(User, null=True, blank=False, related_name='usuario')

    def __str__(self):
        return self.nome + " - " + self.cpf

class Solicitar(models.Model):
    dataHora = models.DateTimeField(blank=True, null=True)
    origem = models.CharField(max_length=128)
    destino = models.CharField(max_length=128)
    departamento = models.ForeignKey(Departamento, null=True, blank=False)
    funcionarios = models.ManyToManyField(Funcionario, null=True, blank=True)

    def __str__(self):
        return self.origem + " - " + self.destino

class Atender(models.Model):
    confirma = models.BooleanField('Confirma')
    solicitacao = models.OneToOneField(Solicitar, null=True, blank=True)
    motorista = models.ForeignKey(Motorista, null=True, blank=True)
    veiculo = models.ForeignKey(Veiculo, null=True, blank=True)

    def __str__(self):
        return str(self.confirma)
# Create your models here.
