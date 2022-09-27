from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models

from .pergunta_multipla_escolha import PerguntaMultiplaEscolha
from .pergunta_objetiva import PerguntaObjetiva


class Alternativa(models.Model):
    '''
        Classe Alternativa implementa as funções relacionadas as alternativas
        de uma pergunta objetiva.
    '''

    titulo = models.CharField(
        verbose_name='Título',
        max_length=250
    )

    descricao = models.TextField(
        verbose_name='Descrição',
        null=True, blank=True
    )

    pergunta_objetiva = models.ForeignKey(
        PerguntaObjetiva,
        verbose_name='Pergunta Objetiva',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    pergunta_multipla_escolha = models.ForeignKey(
        PerguntaMultiplaEscolha,
        verbose_name='Pergunta de múltipla escolha',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    valor = models.IntegerField(
        verbose_name='Valor',
        default=0,
        help_text='Necessário somente se a pergunta for de múltipla escolha'
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de Criação',
        auto_now_add=True
    )

    data_alteracao = models.DateTimeField(
        verbose_name='Data de alteração',
        auto_now=True
    )

    usuario_criacao = models.ForeignKey(
		User,
		related_name='%(class)s_requests_created',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)

    usuario_atualizacao = models.ForeignKey(
		User,
		related_name='%(class)s_requests_modified',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)

    @property
    def escolhida(self):
        '''
        Property para saber se uma alternativa foi
        escolhida por algum usuário.
        '''
        pass

    def __str__(self):
       return self.titulo

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Alternativa, self).save(*args, **kwargs)
        
    class Meta:
        app_label = 'perguntas'
        verbose_name = 'Alternativa'
        verbose_name_plural = 'Alternativas'
