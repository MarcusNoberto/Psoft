# from .alternatina import Alternativa
from crum import get_current_user
from curso.models import Modulo
from django.contrib.auth.models import User
from django.db import models


class PerguntaObjetiva(models.Model):
    '''
        Classe PerguntaObjetiva implementa as funções relacionadas as perguntas objetivas.
        Perguntas objetivas são perguntas que possuem várias alternativas, sendo que apenas uma delas é correta.
    '''

    titulo = models.CharField(
        max_length=250,
        verbose_name='Título'
    )

    descricao = models.TextField(
        verbose_name='Descrição',
        null=True, blank=True
    )

    alternativa_correta = models.ForeignKey(
        'perguntas.Alternativa',
        verbose_name='Alternativa correta',
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

    modulo = models.ForeignKey(
        Modulo,
        verbose_name='Módulo',
        null=True,
        on_delete=models.SET_NULL,
    )

    ordem = models.IntegerField(
        verbose_name='Ordem'
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name='Data de atualização',
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
    def tipo(self):
        '''
        Property usada para que possamos fazer verificações na sibedar
        '''
        return 'pergunta_objetiva'

    @property
    def respondida(self):
        '''
        Property para dizer se o usuário atual respondeu a pergunta ou não
        '''
        return self.resposta_set.filter(
            usuario=get_current_user()
        ).exists()

    @property
    def respondeu_correto(self):
        alternativa_escolhida = self.resposta_set.filter(usuario=get_current_user()).last()
        if alternativa_escolhida and alternativa_escolhida == self.alternativa_correta :
            return True
        else:
            return False

    def __str__(self):
       return '{} | Módulo {}'.format(self.titulo, self.modulo)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(PerguntaObjetiva, self).save(*args, **kwargs)

    class Meta:
        app_label = 'perguntas'
        verbose_name = 'Pergunta objetiva'
        verbose_name_plural = 'Perguntas objetivas'
