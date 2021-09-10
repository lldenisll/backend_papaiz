from django.db import models
from django.contrib.auth.models import User
from banco_de_dados.models import Exame 
from .model_use import *

def user_directory_path(instance, filename):
    return 'images/teste_sexo/{0}'.format(filename)


class Teste(models.Model):

    panoramica  = models.ImageField(upload_to=user_directory_path)
    n_os        = models.CharField(max_length=10, null=True, blank=True)
    sexo_banco  = models.CharField(max_length=10, null=True, blank=True)
    sexo_modelo = models.CharField(max_length=10, null=True, blank=True)
    resultado   = models.BooleanField()
    autor       = models.ForeignKey(User,on_delete=models.PROTECT, related_name='autor_teste_sexo')
    conf_fem    = models.FloatField(null=True, blank=True)
    conf_masc   = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.n_os = self.panoramica.name[:10]
        self.sexo_banco = Exame.objects.get(cd_exame = self.n_os.lower()).sg_sexo
        self.conf_fem = predict_sexo(self.panoramica)[0][0]
        self.conf_masc = predict_sexo(self.panoramica)[0][1]
        if self.conf_fem > self.conf_masc:
            self.sexo_modelo = 'feminino'
        else:
            self.sexo_modelo = 'masculino'
        if self.sexo_modelo == self.sexo_banco:
            self.resultado = True
        else:
            self.resultado = False
        super(Teste, self).save(*args, **kwargs)
    def __str__(self):
        return self.panoramica.name




# Create your models here.
