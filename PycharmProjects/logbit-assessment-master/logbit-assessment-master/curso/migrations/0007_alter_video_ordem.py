# Generated by Django 3.2.4 on 2022-01-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_auto_20220110_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='ordem',
            field=models.IntegerField(default=1, null=True, verbose_name='Ordem'),
        ),
    ]
