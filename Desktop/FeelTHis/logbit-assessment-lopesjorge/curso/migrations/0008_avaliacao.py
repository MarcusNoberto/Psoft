# Generated by Django 3.2.4 on 2022-01-10 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curso', '0007_alter_video_ordem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Nota')),
                ('feedback', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('usuario_atualizacao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='avaliacao_requests_modified', to=settings.AUTH_USER_MODEL)),
                ('usuario_criacao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='avaliacao_requests_created', to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='curso.video', verbose_name='Vídeo')),
            ],
            options={
                'verbose_name': 'Avaliação - Vídeo',
                'verbose_name_plural': 'Avaliações - Vídeos',
            },
        ),
    ]
