from django.db import models
from django.contrib.auth.models import User
from banco_de_dados.models import Exame 
from .helper import *
from. model_use import *

def user_directory_path(instance, filename):
    return 'images/teste_tipo_den/{0}'.format(filename)


class Teste(models.Model):
    panoramica      = models.ImageField(upload_to=user_directory_path)
    n_os            = models.CharField(max_length=10, null=True, blank=True)
    denticao        = models.CharField(max_length=15, null=True, blank=True)
    denticao_modelo = models.CharField(max_length=15, null=True, blank=True)
    resultado       = models.BooleanField()
    autor           = models.ForeignKey(User,on_delete=models.PROTECT, related_name='autor_teste_tipo_den')
    conf_mista      = models.FloatField(null=True, blank=True)
    conf_permanente = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.n_os = self.panoramica.name[:10]
        self.denticao = get_denticao(self.n_os)
        self.conf_mista = predict_den(self.panoramica)[0][0]
        self.conf_permanente = predict_den(self.panoramica)[0][1]
        if self.conf_mista > self.conf_permanente:
            self.denticao_modelo = 'mista'
        else:
            self.denticao_modelo = 'permanente'
        if self.denticao == self.denticao_modelo:
            self.resultado = True
        else:
            self.resultado = False
        super(Teste, self).save(*args, **kwargs)
    def __str__(self):
        return self.panoramica.name
# Create your models here.
