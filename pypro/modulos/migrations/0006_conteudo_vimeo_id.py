# Generated by Django 3.0.7 on 2020-07-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_conteudo'),
    ]

    operations = [
        migrations.AddField(
            model_name='conteudo',
            name='vimeo_id',
            field=models.CharField(default='1', max_length=32),
        ),
    ]
