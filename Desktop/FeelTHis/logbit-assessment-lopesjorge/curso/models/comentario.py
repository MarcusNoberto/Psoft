from django.db import models
from crum import get_current_user
from .video import Video

class Comentario(models.Model):
    comentario = models.TextField(
        verbose_name="Comentario",
        null=True, blank=True
    )

    resposta_comentario = models.ForeignKey(
        'Comentario',
        verbose_name='Resposta para o comentário',
        related_name='resposta_comentario_set', # Só funcionou com um nome diferente :broke_heart:
        null=True, blank=True,
        on_delete=models.SET_NULL
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

    def __str__(self):
       return self.comentario

    def save(self, *args, **kwargs):

        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Comentario, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "curso"
        verbose_name = "Comentário - Vídeo"
        verbose_name_plural = "Comentários - Vídeos"


    