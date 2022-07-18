from collections import namedtuple
from itertools import chain

from crum import get_current_user
from django.db import models
from django.db.models import Value
from django.utils.functional import cached_property
from funcoes_utilitarias import calcular_porcentagem

from ..managers import ModuloManager
from .curso import Curso


class Modulo(models.Model):
    """
        Classe Modulo engloba por partes os vídeos
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

    ordem = models.IntegerField(
        verbose_name="Ordem",
        default=1,
        null=True
    )

    curso = models.ForeignKey(
        Curso,
        verbose_name="Módulo",
        on_delete=models.SET_NULL,
        null=True,
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

    objects = ModuloManager()

    """ @property
    def score(self): """
        

    @cached_property
    def modulo_concluido(self):
        return True if self.progresso_modulo().progresso_total == 100 else False
    
    @cached_property
    def pontuacao_maxima(self):
        score = self.score()
        return score.pontuacao_maxima
    
    @cached_property
    def class_sidebar(self):
        if self.modulo_concluido or not self.has_itens:
            return 'done'
        else:
            ultimo_antes_desse = self.curso.modulo_set.filter(id__lt=self.id).last()
            if not ultimo_antes_desse or ultimo_antes_desse.class_sidebar == 'done':
                return 'doing'
            else:
                return 'disabled'
    
    @cached_property
    def ultimo_item(self):
        try:
            return self.get_all_itens().all_itens[-1] # Se não tiver nenhum item quebra
        except:
            return None
    
    @cached_property
    def has_itens(self):
        if self.get_all_itens().all_itens:
            return True
        else:
            return False 

    def assessments_desse_modulo(self):
        return self.assessment_set.all()

    def videos_desse_modulo(self):
        Videos = namedtuple('Videos', [
            'lista_videos',
            'total_videos',
            'quantidade_videos_concluidos',
            'progresso_videos',
        ])
        
        videos = self.video_set.all()
        total_videos_concluidos = self.total_videos_concluidos(videos)

        return Videos(
            list(videos), # lista_videos
            len(videos), # total_videos
            total_videos_concluidos, # quantidade_videos_concluidos
            calcular_porcentagem(total_videos_concluidos, len(videos)) # progresso_videos
        )

    def total_videos_concluidos(self, videos=None):
        videos = self.video_set.all() if not videos else videos
        user = get_current_user()
        return videos.filter(usuarios_concluintes=user).count()

    def total_perguntas_respondidas(self, perguntas):
        user = get_current_user()
        total = 0
        for pergunta in perguntas:
            if pergunta.resposta_set.filter(usuario=user).exists():
                total += 1
        
        # Outra forma, porém muito confusa 
        # len(list(filter(lambda pergunta: user in pergunta.usuarios_responderam.all(), perguntas)))
        
        return total

    def perguntas_desse_modulo(self):
        Perguntas = namedtuple('Perguntas', [
            'lista_perguntas',
            'total_perguntas',
            'quantidade_perguntas_respondidas',
            'progresso_perguntas',
        ])
        
        perguntas = self.get_perguntas()
        total_perguntas_respondidas = self.total_perguntas_respondidas(perguntas)
        
        return Perguntas(
            perguntas, # lista_perguntas
            len(perguntas), # total_perguntas
            total_perguntas_respondidas, # quantidade_perguntas_respondidas
            calcular_porcentagem(total_perguntas_respondidas, len(perguntas)) # progresso_perguntas
        )
    
    def get_perguntas(self):
        return list(
            self.perguntamultiplaescolha_set.annotate(
                url_redirect=Value('responder_pergunta')
            ).all()
        )

    def progresso_modulo(self):
        videos = self.videos_desse_modulo()
        perguntas = self.perguntas_desse_modulo()
        
        Progresso = namedtuple('Progresso', [
            'videos',
            'perguntas',

            'itens_pendentes',
            'itens_concluidos',
            'total_itens',

            'progresso_total',
        ])

        total_videos_perguntas = videos.total_videos + perguntas.total_perguntas
        total_videos_perguntas_concluidos = videos.quantidade_videos_concluidos + perguntas.quantidade_perguntas_respondidas
        total_videos_perguntas_pendentes = total_videos_perguntas - total_videos_perguntas_concluidos

        return Progresso(
            videos, # videos
            perguntas, # perguntas
            
            total_videos_perguntas_pendentes, # itens_pendentes
            total_videos_perguntas_concluidos, # itens_concluidos
            total_videos_perguntas, # total_itens
            
            calcular_porcentagem(total_videos_perguntas_concluidos, total_videos_perguntas) # progresso_total
        )

    def quantas_usuario_acertou_do_modulo(self):
        user = get_current_user()
        from ...respostas.models import Resposta
        respostas = Resposta.objects.filter(usuario = user)
        return len(list(filter(lambda resposta:resposta.correta, respostas)))
    
    def get_all_itens(self: object) -> list:
        '''
        Função para retornar uma lista com todas as perguntas
        e todos os vídeos do módulo.
        '''
        Itens = namedtuple('Itens', [
            'all_itens',
            'names',
        ])

        all_itens = list(chain(
            self.get_perguntas(),
            self.video_set.annotate(
                url_redirect=Value('video:video')
            ).all()
        ))
        all_itens = sorted(all_itens, key=lambda item: item.ordem)
        
        return Itens(
            all_itens,
            self.get_all_itens_names(all_itens)
        )
    
    def get_all_itens_names(self, all_itens):
        names = ''
        for item in all_itens:
            names += '{} '.format(item)
        
        return names
    
    def score(self):
        Score = namedtuple('Score', [
            'pontuacao_usuario',
            'pontuacao_maxima',
            'porcentagem',
        ])

        usuario = get_current_user()
        pontuacao_usuario = usuario.resposta_set.pontuacao_usuario(usuario, modulo=self)
        pontuacao_maxima = self.perguntamultiplaescolha_set.nota_maxima_perguntas()
        
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
        super(Modulo, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "curso"
        verbose_name = "Capítulo"
        verbose_name_plural = "Capítulos"
