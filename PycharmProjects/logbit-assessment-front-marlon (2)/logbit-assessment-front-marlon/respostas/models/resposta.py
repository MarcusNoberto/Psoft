#Shift + Alt + O para organizar as importações (vs code)

from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models
from perguntas.models import PerguntaMultiplaEscolha, PerguntaObjetiva

from ..managers import RespostaManager


class Resposta(models.Model):
    '''
    A classe resposta serve para armazenar todas as respostas de cada usuário.
    Além de desempenhar funcionalidades relecionadas a uma resposta.
    '''

    #ANCHOR Dados da resposta
    resposta = models.CharField(
        verbose_name='Resposta',
        max_length=255
    )

    #ANCHOR Dados dos usuários
    usuario = models.ForeignKey(
        User,
        verbose_name='Usuário',
        related_name='resposta_set',
        null=True,
        on_delete=models.SET_NULL
    )

    usuario_atualizacao = models.ForeignKey(
        User,
        verbose_name='Usuário de atualização',
        related_name='usuario_atualizacao',
        null=True,
        on_delete=models.SET_NULL
    )

    #ANCHOR Dados das perguntas
    pergunta_multipla_escolha = models.ForeignKey(
        PerguntaMultiplaEscolha,
        verbose_name='Pergunta multipla escolha',
        null=True,
        on_delete=models.SET_NULL
    )

    pergunta_objetiva = models.ForeignKey(
        PerguntaObjetiva,
        verbose_name='Pergunta objetiva',
        null=True,
        on_delete=models.SET_NULL
    )

    pontuacao = models.IntegerField(
        verbose_name='Pontuação',
        default=0
    )

    #ANCHOR Dados das datas
    data_criacao = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name='Data de atualização',
        auto_now=True
    )

    objects = RespostaManager()

    #ANCHOR Properties
    @property
    def pergunta(self):
        return self.pergunta_multipla_escolha or self.pergunta_objetiva

    @property
    def correta(self):
        if self.pergunta_objetiva:
            alternativa_correta = self.pergunta_objetiva.alternativa_correta
            if alternativa_correta:
                return True if alternativa_correta.titulo == self.resposta else False
        return False
    
    @property
    def curso(self):
        try:
            return self.pergunta.modulo.curso
        except:
            return None

    #ANCHOR Métodos
    def set_pontuacao(self):
        if self.pergunta:
            alternativa_marcada = self.pergunta.alternativa_set.filter(titulo=self.resposta).first()
            if alternativa_marcada and alternativa_marcada.valor != self.pontuacao:
                self.pontuacao = alternativa_marcada.valor
                self.save()

    def __str__(self):
        return self.resposta

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario = user
        self.usuario_atualizacao = user
        super(Resposta, self).save(*args, **kwargs)

    #ANCHOR Classes
    class Meta:
        app_label = 'respostas'
        verbose_name = 'resposta'
        verbose_name_plural = 'Respostas'
