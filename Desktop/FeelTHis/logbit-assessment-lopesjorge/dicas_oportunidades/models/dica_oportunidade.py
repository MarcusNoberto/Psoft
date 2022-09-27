#Shift + Alt + O para organizar as importações (vs code)

from curso.models import Video
from django.db import models
from perguntas.models import PerguntaMultiplaEscolha, PerguntaObjetiva


class DicaOportunidade(models.Model):
    '''
    Classe para registrarmos as dicas e oportunidades
    do sistema, além de fazer as funcionalidades
    relacionadas a uma dica/oportunidade
    '''

    pergunta_multipla_escolha = models.ForeignKey(
        PerguntaMultiplaEscolha,
        verbose_name='Pergunta multipla escolha',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    pergunta_objetiva = models.ForeignKey(
        PerguntaObjetiva,
        verbose_name='Pergunta objetiva',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    dica = models.TextField(
        verbose_name='Dica',
        null=True
    )

    aula_sugerida = models.ForeignKey(
        Video,
        verbose_name='Aula sugerida',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True,
        null=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name='Data de atualização',
        auto_now=True,
        null=True
    )

    @property
    def pergunta(self):
        return self.pergunta_multipla_escolha or self.pergunta_objetiva
    
    def __str__(self):
        return '{}'.format(self.dica)

    class Meta:
        app_label = 'dicas_oportunidades'
        verbose_name = 'Dica e oportunidade'
        verbose_name_plural = 'Dicas e oportunidades'
