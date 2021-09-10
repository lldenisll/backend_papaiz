# Generated by Django 3.2.5 on 2021-08-12 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelo_sexo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panoramica', models.ImageField(upload_to=modelo_sexo.models.user_directory_path)),
                ('n_os', models.CharField(blank=True, max_length=10, null=True)),
                ('sexo', models.CharField(blank=True, max_length=10, null=True)),
                ('resultado', models.BooleanField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='autor_teste_sexo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
