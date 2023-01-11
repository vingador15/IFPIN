import datetime
from Mapa.models import Local
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from smart_selects.db_fields import GroupedForeignKey


class Sala(models.Model):

    AULA = 'Aula'
    ADMIN = 'Admin'

    FUNCAO = (
        (AULA, 'Aula'),
        (ADMIN, 'Admin')
    )

    Numero = models.IntegerField()
    Funcao = models.CharField(max_length=50, choices=FUNCAO)
    Comprimento = models.CharField(max_length=10, null=True, blank=True)
    Altura = models.CharField(max_length=10, null=True, blank=True)
    Profundidade = models.CharField(max_length=10, null=True, blank=True)
    Disponibilidade = models.CharField(max_length=50)
    Lugar = models.ForeignKey(Local, on_delete=models.CASCADE)
    criado_em = models.DateTimeField("Criado em",default=timezone.now)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=timezone.now)
    

    def __str__(self):
        return '%d' % (self.Numero)

    def criado_em(self):
        return self.criado_em >= timezone.now() - datetime.timedelta(days=1)


'''class Local(models.Model):
    Nome = models.CharField(max_length=100, unique=True)
    Referencia = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField("Criado em",default=timezone.now)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=timezone.now)

    def __str__(self):
        return self.Nome

    def criado_em(self):
        return self.criado_em >= timezone.now() - datetime.timedelta(days=1)
'''

class Espaco(models.Model):
    criado_em = models.DateTimeField("Criado em",default=timezone.now)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=timezone.now)
    
    class Meta:
        abstract = True

    def criado_em(self):
        return self.criado_em >= timezone.now() - datetime.timedelta(days=1)
    
class Turma(Espaco):

    INTEGRAL = 'Integral'
    MANHA = 'Manhã'
    TARDE = 'Tarde'
    NOITE = 'Noite'
    
    TURNO = (
        (INTEGRAL, 'Integral'),
        (MANHA, 'Manhã'),
        (TARDE, 'Tarde'),
        (NOITE, 'Noite'),
    )
    Salas = models.ForeignKey(Sala, on_delete=models.CASCADE)
    #Horario = models.ImageField()
    Numero = models.IntegerField(unique=True)
    Curso = models.CharField(max_length=50)
    Turno = models.CharField(max_length=8,choices=TURNO)

    def clean(self):
        if self.Salas.Funcao != 'Aula':
            raise ValidationError(_('Sala Não Suporta Turma')) 

    def __str__(self):
        return '%d' % (self.Numero)
    

class AdminEscola(Espaco):
    Salas = models.ForeignKey(Sala, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=50, unique=True)
    Funcao = models.CharField(max_length=100)
    Email = models.EmailField()
    
    
    def clean(self):
        if self.Salas.Funcao != 'Admin':
            raise ValidationError(_('Sala Não Suporta Admininistração da Escola')) 


    def __str__(self):
        return self.Nome

class Produto(models.Model):

    APROVADO = 'Aprovado'
    ANALISE = 'Análise'
    REPROVADO = 'Reprovado'

    STATUS = (
        (APROVADO, 'Aprovado'),
        (ANALISE, 'Análise'),
        (REPROVADO, 'Reprovado')
    )
    Lugar = models.ForeignKey(Local, on_delete=models.CASCADE)
    Salas = GroupedForeignKey(Sala, "Lugar")
    Pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    NomeProduto = models.CharField(max_length=50, db_column='Nome do Produto')
    NomePessoa = models.CharField(max_length=50)
    Situação = models.CharField(max_length=9, choices=STATUS, default='Análise')
    Valor = models.FloatField(db_column='R$')

    def __str__(self):
        return self.NomeProduto

#comando pra tornar o shell mais dinâmico
'''import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
import django
django.setup()'''
