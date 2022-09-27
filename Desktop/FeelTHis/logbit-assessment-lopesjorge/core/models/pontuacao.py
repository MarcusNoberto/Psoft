from django.db import models


class Pontuacao(models.Model):
    '''
    A classe Pontuacao serve para armazernar os(as) nome da sua model do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Pontuacao.
    '''

    pontuacao_bronze = models.FloatField(
        verbose_name='Pontuação Bronze',
        null = False,
        blank = False,
        default = 33.3
    )

    pontuacao_prata = models.FloatField(
        verbose_name='Pontuação prata',
        null = False,
        blank = False,
        default = 66.6
    )

    pontuacao_ouro = models.FloatField(
        verbose_name='Pontuação Ouro',
        null = False,
        blank = False,
        default = 66.7
    )

    class Meta:
        app_label = 'core'
        verbose_name = 'Pontuação'
        verbose_name_plural = 'Pontuações'
