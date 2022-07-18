from collections import namedtuple

from crum import get_current_user
from django.db import models
from funcoes_utilitarias.our_math import calcular_porcentagem


class Curso(models.Model):
    """
        Classe Curso engloba por partes os módulos
    """

    titulo = models.CharField(
        max_length=250,
        verbose_name="Título",
        help_text="Campo Obrigatório"
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        null=True, blank=True
    )

    foto_capa = models.ImageField(
        verbose_name='Foto de capa',
        help_text = 'Resolução sugerida 320 x 450',
        blank=True, null=True
    )

    usuarios_com_acesso = models.ManyToManyField(
		'auth.User', 
        verbose_name=('Usuários com acesso'),
        blank=True,
    )

    data_alteracao = models.DateTimeField(
        verbose_name="Data de Alteração",
        auto_now=True
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    usuario_criacao = models.ForeignKey(
		'auth.User', 
		related_name='%(class)s_requests_created',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)

    usuario_atualizacao = models.ForeignKey(
		'auth.User', 
		related_name='%(class)s_requests_modified',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)

    pre_requisito = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name= 'Pré-requisitos',
        blank=True, null=True,
    )

    score_minimo = models.IntegerField(
        verbose_name='Score mínimo',
        blank=True, null=True,
        default=75
    )

    progresso_minimo = models.IntegerField(
        verbose_name='Progresso mínimo',
        blank=True, null=True,
        default=90
    )
    
    @property
    def curso_concluido(self):
        user = get_current_user()
        concluido=False

        if len(self.modulo_set.all())>0 and user:
            concluido=True
            for modulo in self.modulo_set.all():
                if not modulo.modulo_concluido:
                    concluido=False

        return concluido

    @property
    def atingiu_pre_requisito(self):
        for curso in self.pre_requisito.all():
            if curso.score().porcentagem < curso.score_minimo or curso.progresso_total_modulos() < curso.progresso_minimo:
                return False

        return True
    
    @property
    def ultimo_item(self):
        all_lasts_itens = []
        for modulo in self.modulo_set.all():
            if modulo.ultimo_item:
                all_lasts_itens.append(modulo.ultimo_item)
        return all_lasts_itens[-1]

    
    def progresso_total_modulos(self, modulos=None):
        modulos = self.modulo_set.all() if not modulos else modulos
        total_progresso_todos_modulos = 0
        
        for modulo in modulos:
            progresso_modulo = modulo.progresso_modulo()
            total_progresso_todos_modulos += progresso_modulo.progresso_total

        progresso_total = total_progresso_todos_modulos / (len(modulos) or 1)
        return round(progresso_total, 2)
    
    def progresso_curso(self):
        Modulos = namedtuple('Modulos', [
            'lista_modulos',
            'total_modulos',
            'quantidade_modulos_concluidos',
            'progresso_total',
        ])

        modulos = self.modulo_set.all()

        return Modulos(
            modulos, # lista_modulos
            len(modulos), # total_modulos
            self.modulo_set.total_modulos_concluidos(), # quantidade_modulos_concluidos
            self.progresso_total_modulos(modulos) # progresso_total
        )
    
    def score(self):
        Score = namedtuple('Score', [
            'pontuacao_usuario',
            'pontuacao_maxima',
            'porcentagem',
        ])

        usuario = get_current_user()
        pontuacao_usuario = usuario.resposta_set.pontuacao_usuario(usuario, curso=self)
        pontuacao_maxima = self.modulo_set.nota_maxima_modulos()

        return Score(
            pontuacao_usuario,
            pontuacao_maxima,
            calcular_porcentagem(pontuacao_usuario, pontuacao_maxima)
        )

    def __str__(self):
       return self.titulo

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Curso, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "curso"
        verbose_name = "Módulo"
        verbose_name_plural = "Módulos"
