from django.db import models


class Exame(models.Model):
    id_exame = models.IntegerField(primary_key=True)
    dt_exame = models.DateField()
    sg_sexo = models.CharField(max_length=10)
    dt_idade = models.DateField()
    cd_exame = models.CharField(max_length=10, unique = True)
    def __str__(self):
        return self.cd_exame

class Exame_alt_anatomia(models.Model):
    id_exame = models.IntegerField(primary_key=True)
    id_alteracao = models.IntegerField()
    def __str__(self):
        return self.id_exame
# Create your models here.
