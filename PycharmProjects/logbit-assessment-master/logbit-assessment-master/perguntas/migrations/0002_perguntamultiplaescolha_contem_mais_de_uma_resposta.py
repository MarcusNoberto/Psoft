# Generated by Django 3.2.4 on 2022-02-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perguntamultiplaescolha',
            name='contem_mais_de_uma_resposta',
            field=models.BooleanField(default=False, verbose_name='Essa pergunta contém mais de uma resposta certa?'),
        ),
    ]
