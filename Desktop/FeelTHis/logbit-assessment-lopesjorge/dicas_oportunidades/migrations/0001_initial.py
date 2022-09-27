# Generated by Django 3.2.4 on 2022-02-04 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DicasOportunidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', django_quill.fields.QuillField()),
            ],
        ),
        migrations.CreateModel(
            name='DicasDirecionadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dicas_oportunidades.dicasoportunidades', verbose_name='Descricao')),
                ('lido_por', models.ManyToManyField(blank=True, null=True, related_name='lido', to=settings.AUTH_USER_MODEL, verbose_name='Lido por')),
                ('usuarios_direcionados', models.ManyToManyField(blank=True, null=True, related_name='direcionados', to=settings.AUTH_USER_MODEL, verbose_name='Usuários direcionados')),
            ],
        ),
    ]
