# Generated by Django 3.2.4 on 2022-08-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0004_perguntamultiplaescolha_aula_relacionada'),
    ]

    operations = [
        migrations.AddField(
            model_name='perguntamultiplaescolha',
            name='pontuacao_bronze',
            field=models.FloatField(default=33.3, verbose_name='Pontuação Bronze'),
        ),
        migrations.AddField(
            model_name='perguntamultiplaescolha',
            name='pontuacao_ouro',
            field=models.FloatField(default=80.0, verbose_name='Pontuação Ouro'),
        ),
        migrations.AddField(
            model_name='perguntamultiplaescolha',
            name='pontuacao_prata',
            field=models.FloatField(default=66.6, verbose_name='Pontuação prata'),
        ),
    ]
