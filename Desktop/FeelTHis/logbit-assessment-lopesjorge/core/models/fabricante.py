from django.db import models


class Fabricante(models.Model):
    '''
    A classe Fabricante serve para armazernar os(as) fabricantes do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Fabricante.
    '''

    nome_fabricante = models.CharField(
        verbose_name='Nome do Fabricante',
        max_length=255
    )

    nome_auth = models.CharField(
        verbose_name='Nome no Auth',
        max_length=255
    )

    CHOICES_LINGUAGEM = [
        ('PT', 'PT'),
        ('ES', 'ES'),
        ('EN', 'EN')
    ]

    linguagem = models.CharField(
        verbose_name='Linguagem',
        max_length=7,
        choices=CHOICES_LINGUAGEM,
        null=True,
        default='PT'
    )

    def __str__(self):
        return self.nome_fabricante
    
    class Meta:
        app_label = 'core'
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'
        ordering=('nome_fabricante', 'id')
