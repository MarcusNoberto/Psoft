# Generated by Django 3.2.4 on 2022-02-11 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracao_assessment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracaoanexo',
            name='configuracao_etapa',
        ),
        migrations.AddField(
            model_name='configuracaoanexo',
            name='configuracao_assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='configuracao_assessment.configuracaoassessment', verbose_name='Configuração Assessment'),
        ),
    ]
