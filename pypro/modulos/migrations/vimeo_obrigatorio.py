# Generated by Django 3.0.7 on 2020-07-01 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_conteudo_vimeo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conteudo',
            name='vimeo_id',
            field=models.CharField(max_length=32),
        ),
    ]
