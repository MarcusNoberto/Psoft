from collections import namedtuple

from crum import get_current_user
from django.db import models
from django.core.exceptions import ValidationError
from funcoes_utilitarias.our_math import calcular_porcentagem
from .projeto import Projeto


class Curso(models.Model):
    """
        Classe Curso engloba por partes os módulos
    """

    titulo = models.CharField(
        max_length=250,
        verbose_name="Título",
        help_text="Campo Obrigatório"
    )
    

    CHOICES_LINGUAGEM = [
        ('PT', 'PT'),
        ('ES', 'ES'),
        ('EN', 'EN')
    ]

    projeto = models.ForeignKey(
        Projeto,
        on_delete = models.SET_NULL,
        null = True
    )

    linguagem = models.CharField(
        verbose_name='Linguagem',
        max_length=7,
        choices=CHOICES_LINGUAGEM,
        default='PT'
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        null=True, blank=True
    )

    icone = models.CharField(
        verbose_name='icone',
        max_length=70,
        null=True, blank=True,
        help_text='Copie e cole um ícone da <a target="_blank" href="https://ionic.io/ionicons">ionicons</a> ou <a target="_blank" href="https://fontawesome.com/v4/icons/">Font Awesome 4</a>'
    )

    foto_capa = models.ImageField(
        verbose_name='Foto de capa',
        help_text = 'Resolução sugerida 320 x 450',
        blank=True, null=True
    )

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

    @property
    def ultimo_modulo(self):
        return self.modulo_set.all().last()

    
    def progresso_total_modulos(self, modulos=None):
        modulos = self.modulo_set.all() if not modulos else modulos
        total_progresso_todos_modulos = 0
        
        for modulo in modulos:
            progresso_modulo = modulo.progresso_modulo()
            total_progresso_todos_modulos += progresso_modulo.progresso_total

        progresso_total = total_progresso_todos_modulos / (len(modulos) or 1)
        return round(progresso_total, 2)

    @property
    def get_progresso_perguntas(self):
        modulo = self.modulo_set.all().first()
        return modulo.perguntas_desse_modulo().progresso_perguntas
    
    @property
    def primeiro_modulo(self):
        return self.modulo_set.all().first()

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
    @property
    def get_porcentagem_progresso(self):
        from .modulo import Modulo
        somador  = 0
        aux = 0
        for modulo in Modulo.objects.filter(curso = self):
            somador += modulo.progresso_modulo().progresso_total
            aux +=1
        porcentagem = somador/(aux or 1)
        return str(porcentagem).replace(',','.')

    def primeiro_video_modulos(self):
        modulos = self.modulo_set.all()
        videos = []
        for modulo in modulos:
            videos.append(modulo.primeiro_video_do_modulo)
        return videos
    
    @property
    def progresso_curso_relacionado_conquista(self):
        diferenca = 0
        if self.progresso_curso().progresso_total < self.pontuacao_bronze:
            diferenca = self.pontuacao_bronze - self.progresso_curso().progresso_total
        elif self.pontuacao_bronze < self.progresso_curso().progresso_total < self.pontuacao_prata:
            diferenca = self.pontuacao_prata - self.progresso_curso().progresso_total
        else:
            diferenca = 100 - self.progresso_curso().progresso_total
        return round(diferenca)

    
    @property
    def primeiro_video_modulo(self):
        modulos = self.modulo_set.all()
        print(self.modulo_set.all().count())
        print('Teste')
        for modulo in modulos:
            return modulo.primeiro_video_do_modulo
        return None

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

    @property
    def quantidade_perguntas_respondidas(self):
        from respostas.models import Resposta
        usuario = get_current_user()
        respostas = 0
        for resposta in Resposta.objects.filter(usuario=usuario):
            try:
                if resposta.pergunta.modulo.curso == self:
                    respostas += 1
            except:
                pass
        

        return respostas

    @property
    def quantidade_perguntas(self):
        from respostas.models import Resposta
        usuario = get_current_user()
        perguntas = 0
        modulos = self.modulo_set.all()
        for modulo in modulos:
            perguntas+=modulo.perguntas_desse_modulo().total_perguntas
        

        return perguntas

    @property
    def progresso_quizz(self):
        progresso = (self.quantidade_perguntas_respondidas/(self.quantidade_perguntas or 1))*100

        return round(progresso)

    @property
    def progresso_video(self):
        quantidade_aulas = 0
        quantidade_aulas_vistas = 0
        for modulo in self.modulo_set.all():
            quantidade_aulas += modulo.total_videos
            quantidade_aulas_vistas += modulo.total_videos_finalizados

        return (quantidade_aulas_vistas/(quantidade_aulas or 1))*100

    @property
    def primeira_pergunta(self):
        return self.modulo_set.first().primeira_pergunta
        


    def __str__(self):
       return self.titulo

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        
        self.usuario_atualizacao = user
        if (self.pontuacao_bronze > self.pontuacao_prata) or (self.pontuacao_bronze > self.pontuacao_ouro) or (self.pontuacao_prata > self.pontuacao_ouro):
            raise ValidationError("Pontuações inválidas para o programa")
        super(Curso, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "curso"
        verbose_name = "Módulo"
        verbose_name_plural = "Módulos"
