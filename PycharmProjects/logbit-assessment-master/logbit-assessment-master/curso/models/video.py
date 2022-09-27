from django.db import models
from crum import get_current_user
from .modulo import Modulo

class Video(models.Model):
    """
        Classe Video implementa as funções relacionadas aos videos
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
    
    def validate_file_extension(value):
        import os
        from django.core.exceptions import ValidationError
        ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
        valid_extensions = ['.mp4']

        if not ext.lower() in valid_extensions:
            raise ValidationError('Somente arquivos .mp4 são válidos')

    video = models.FileField(
        verbose_name="Vídeo",
        upload_to='video/',
        help_text="Campo Obrigatório",
        validators=[validate_file_extension]

    )

    thumbnail = models.ImageField(
        verbose_name="thumbnail",
        null=True,
        blank=False,
        upload_to='thumbnail/'
    )

    modulo = models.ForeignKey(
        Modulo,
        verbose_name="Capítulo",
        on_delete=models.SET_NULL,
        null=True,
    )

    ordem = models.IntegerField(
        verbose_name="Ordem",
        default=1,
        null=True
    )

    ### Dados de Acesso ###
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
    
    usuarios_concluintes = models.ManyToManyField(
		'auth.User', 
        verbose_name=('Usuários concluintes'),
        blank=True,
    )

    usuario_atualizacao = models.ForeignKey(
		'auth.User', 
		related_name='%(class)s_requests_modified',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)
    ### Dados de Acesso ###

    def conclui_visualizacao(self, usuario):
        self.usuarios_concluintes.add(usuario)
        self.save()

    @property
    def tipo(self):
        '''
        Property usada para que possamos fazer verificações na sibedar
        '''
        return 'video'
    
    @property
    def curso(self):
        if self.modulo:
            return self.modulo.curso or None
        return None
    curso.fget.short_description = 'Módulo'

    @property
    def id_cap(self):
        return self.modulo.id
    
    @property
    def nome_capitulo(self):
        return self.modulo.titulo

    @property
    def nome_modulo(self):
        return self.modulo.curso.titulo
    
    @property
    def id_modulo(self):
        return self.modulo.curso.id

    def __str__(self):
       return '{} | {}'.format(self.titulo, self.modulo)

    def save(self, *args, **kwargs):

        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Video, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "curso"
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"
