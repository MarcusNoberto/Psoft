# Generated by Django 3.2.4 on 2022-01-10 19:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curso', '0013_alter_comentario_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='usuarios_concluintes',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Usuários concluintes'),
        ),
    ]
