# Generated by Django 3.2.5 on 2021-08-11 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo_tipo_den', '0002_teste_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='teste',
            name='denticao',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]