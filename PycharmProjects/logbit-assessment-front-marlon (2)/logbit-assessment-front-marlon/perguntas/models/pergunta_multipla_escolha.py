# from .alternatina import Alternativa
from decimal import Decimal

from crum import get_current_user
from curso.models import Modulo
from django.contrib.auth.models import User
from django.db import models

from ..managers import PerguntaMultiplaEscolhaManager


class PerguntaMultiplaEscolha(models.Model):
    '''
        Classe PerguntaMultiplaEscolha implementa as funções relacionadas
        as perguntas de múltipla escolha.
        Perguntas de múltipla escolha são perguntas que possuem várias alternativas,
        e cada uma dessas alternativas tem uma pontuação.
    '''

    titulo = models.CharField(
        max_length=250,
        verbose_name='Título'
    )

    descricao = models.TextField(
        verbose_name='Descrição',
        null=True, blank=True
    )
    
    valor_minimo = models.IntegerField(
        verbose_name='Valor mínimo',
        default=0,
        help_text='Valor mínimo esperado do aluno'
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

    contem_mais_de_uma_resposta = models.BooleanField(
        default = False,
        verbose_name= "Essa pergunta contém mais de uma resposta certa?",
    )

    objects = PerguntaMultiplaEscolhaManager()

    @property
    def curso(self):
        try:
            return self.modulo.curso
        except:
            return '-'

    @property
    def tipo(self):
        '''
        Property usada para que possamos fazer verificações na sibedar
        '''
        return 'pergunta_multipla_escolha'

    @property
    def respondida(self):
        '''
        Property para dizer se o usuário atual respondeu a pergunta ou não
        '''
        return self.resposta_set.filter(
            usuario=get_current_user()
        ).exists()

    @property
    def pontos_conquistados(self):
        from .alternativa import Alternativa
        nota=0
        user = get_current_user()
        
        try:
            if self.contem_mais_de_uma_resposta:
                
                for resposta in user.resposta_set.filter(pergunta_multipla_escolha=self):
                    nota+=Alternativa.objects.get(titulo=resposta.resposta).valor
            else:
                id_alternativa=user.resposta_set.filter(pergunta_multipla_escolha=self).last().resposta
                nota+=Alternativa.objects.get(titulo=id_alternativa).valor

        except:
            nota=0
        
        return nota

    @property
    def respondeu_correto(self):
        if self.pontos_conquistados >= self.valor_minimo:
            return True
        else:
            return False

    @property
    def alternativa_correta(self):
       return self.alternativa_set.all().order_by('valor').last()

    @property
    def old_nota_maxima(self):
        nota=0
        for alternativa in self.alternativa_set.all():
            if nota<alternativa.valor:
                nota=alternativa.valor
        return nota

    @property
    def nota_maxima(self):
        nota=0
        if self.contem_mais_de_uma_resposta:
            for alternativa in self.alternativa_set.all():
                nota+=alternativa.valor
            return nota
        
        return self.old_nota_maxima
    
    @property
    def score_pergunta(self):
        try:
            return f'{Decimal((self.pontos_conquistados / self.nota_maxima) * 100):.2f}'
        except:
            return f'{Decimal(0):.2f}'

    def __str__(self):
       return '{} | Módulo {}'.format(self.titulo, self.modulo)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(PerguntaMultiplaEscolha, self).save(*args, **kwargs)

    class Meta:
        app_label = 'perguntas'
        verbose_name = 'Pergunta de múltipla escolha'
        verbose_name_plural = 'Perguntas de múltipla escolha'
