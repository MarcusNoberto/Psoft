from django.db import models
from crum import get_current_user
from .video import Video

class AnexoVideo(models.Model):

    titulo = models.CharField(
        max_length=200,
        verbose_name='titulo'
    )

    anexo = models.FileField(
        verbose_name="Anexo",
        upload_to='anexos_videos/',
    )

    video = models.ForeignKey(
        Video,
        verbose_name="Vídeo",
        on_delete=models.SET_NULL,
        null=True,
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
    
    usuario_atualizacao = models.ForeignKey(
		'auth.User', 
		related_name='%(class)s_requests_modified',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)
    ### Dados de Acesso ###
    @property
    def arquivo_size(self):
        size = ''
        if self.anexo and self.anexo.url:
            try:
                size = self.anexo.file.size
            except:
                return size    
            if size < 512000:
                size = '{} KB'.format(
                    round(size / 1024.0, 2)
                )
            elif size < 4194304000:
                size = '{} MB'.format(
                    round(size / 1048576.0, 2)
                )
            else:
                size = '{} GB'.format(
                    round(size / 1073741824.0, 2)
                )
        return size

    @property
    def arquivo_extension(self):
        if self.anexo and self.anexo.url:
            return self.anexo.name.split('.')[-1].upper()
        return ''
    
    @property
    def arquivo_icon(self):
        return 'icon_{}'.format(self.arquivo_extension.lower())

    def __str__(self):
       return self.titulo + ('{}').format(self.id)

    def save(self, *args, **kwargs):

        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(AnexoVideo, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "curso"
        verbose_name = "Anexo - Vídeo"
        verbose_name_plural = "Anexos - Vídeos"

    

    