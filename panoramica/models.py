from django.db import models
from django.contrib.auth.models import User
from .helper import *


def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)


class Panoramica(models.Model):
    panoramica = models.ImageField(upload_to=user_directory_path)
    n_os       = models.CharField(max_length=10, null=True, blank=True)
    autor      = models.ForeignKey(User,on_delete=models.PROTECT, related_name='autor')
    def save(self, *args, **kwargs):
        self.n_os = self.panoramica.name[:10]
        print('nome_os')
        self.panoramica = anonimiza_laudo(self.panoramica)
        super(Panoramica, self).save(*args, **kwargs)
    def __str__(self):
        return self.panoramica.name
# Create your models here.
