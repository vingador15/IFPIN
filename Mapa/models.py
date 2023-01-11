# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Local(models.Model):
    nome = models.CharField(max_length=254)
    referencia = models.CharField(max_length=254, null=True, blank=True)
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return self.nome

    @property
    def popup_content(self):
        #nome = f'<p><strong>Nome:</strong> {self.nome}</p>'
        #ref = f'<p><strong>Referencia:</strong> {self.referencia}</p>'
        nome = self.nome
        referencia = self.referencia
        return f'<strong>Nome:</strong> {self.nome}<br><strong>Referencia:</strong> {self.referencia}'



