from crum import get_current_user
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .video import Video


class Avaliacao(models.Model):
    nota = models.IntegerField(
        verbose_name="Nota",
        validators=[
            MinValueValidator(1, 'A nota deve ser maior que 0'),
            MaxValueValidator(5, 'A nota deve ser menor ou igual a 5')
        ]
    )
    
    feedback = models.TextField(
        verbose_name="Descrição",
        null=True, blank=True
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

    def update_nota(self, nota):
        self.nota = nota
        self.save()

    def __str__(self):
       return 'Avaliação do vídeo {}'.format(self.video) if self.video else 'Avaliação {}'.format(self.id)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Avaliacao, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "curso"
        verbose_name = "Avaliação - Vídeo"
        verbose_name_plural = "Avaliações - Vídeos"


    