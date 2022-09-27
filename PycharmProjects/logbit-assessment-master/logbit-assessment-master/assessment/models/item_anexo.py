from assessment.models.anexo import Anexo
from django.db import models
from crum import get_current_user

class ItemAnexo(models.Model):
    """
       Classe ItemAnexo implementa as funções relacionadas aos itens dos anexos
    """

    arquivo = models.FileField(
        verbose_name="Anexo",
        upload_to ='uploads/',
        blank=True,
    )

    anexo = models.ForeignKey(
        Anexo,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Anexo"
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

    def __str__(self):
       return self.arquivo.name

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(ItemAnexo, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "assessment"
        verbose_name = "Item Anexo"
        verbose_name_plural = "Itens Anexos"