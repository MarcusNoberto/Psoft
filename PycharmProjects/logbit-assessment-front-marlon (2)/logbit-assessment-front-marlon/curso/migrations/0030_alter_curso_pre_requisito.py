# Generated by Django 3.2.4 on 2022-02-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0029_merge_20220217_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='pre_requisito',
            field=models.ManyToManyField(blank=True, null=True, to='curso.Curso', verbose_name='Pré-requisito'),
        ),
    ]
