# Generated by Django 3.2.5 on 2021-08-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id_exame', models.IntegerField(primary_key=True, serialize=False)),
                ('dt_exame', models.DateField()),
                ('sg_sexo', models.CharField(max_length=10)),
                ('dt_idade', models.DateField()),
                ('cd_exame', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]