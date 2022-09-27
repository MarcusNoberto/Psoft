from django.db import models


class Traducao(models.Model):
    '''
    A classe Traducao serve para armazernar os(as) traduções do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Traducao.
    '''
    espanhol = models.CharField(
        verbose_name="Español",
        max_length=1000,
        null=True,
    )
    
    portugues = models.CharField(
        verbose_name="Português",
        max_length=1000,
        null=True,
        unique=True
    )

    ingles = models.CharField(
        verbose_name="English",
        max_length=1000,
        null=True,
    )

    def __str__(self):
        return self.espanhol

    class Meta:
        app_label = 'core'
        verbose_name = 'Tradução'
        verbose_name_plural = 'Traduções'
