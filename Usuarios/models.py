from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    DOCENTE = 'Docente'
    DISCENTE = 'Discente'
    VISITANTE = 'Visitante'

    TIPO = [
        (DOCENTE, 'Docente'),
        (DISCENTE, 'Discente'),
        (VISITANTE, 'Visitante')
    ]

    Nome = models.CharField(max_length=100, null=True, verbose_name='Primeiro Nome')
    UltimoNome = models.CharField(max_length=100, null=True, verbose_name='Ultimo Nome')
    TipoUsuario = models.CharField(max_length=9, null=True, verbose_name='Tipo de Usuário', choices=TIPO)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Foto = models.ImageField(upload_to='img/%y', null=True, blank=True)

    def __str__(self):
        return self.Nome
     
    