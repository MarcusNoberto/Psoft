# Generated by Django 3.2.4 on 2022-01-10 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curso', '0002_modulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Campo Obrigatório', max_length=250, verbose_name='Título')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('usuario_atualizacao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='curso_requests_modified', to=settings.AUTH_USER_MODEL)),
                ('usuario_criacao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='curso_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
    ]
