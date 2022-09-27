from django.db import models
from datetime import datetime
from colorfield.fields import ColorField
from crum import get_current_user

class Empresa(models.Model):
    """
       Classe Empresa implementa as funções relacionadas a uma empresa
    """

    nome = models.CharField(
		max_length=250,
		verbose_name="Nome",
		help_text="Campo Obrigatório*"
	)

    cnpj = models.CharField(
        max_length=19,
        verbose_name="CNPJ",
        help_text="Campo Obrigatório"
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True, null=True
    )

    cor_principal = ColorField(
        default='#FFFFFF', 
    )

    cor_secundaria = ColorField(
        default='#FFFFFF', 
    )

    logo = models.ImageField(
        verbose_name='Logo',
        null=True, blank=True
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
        return self.nome

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Empresa, self).save(*args, **kwargs)

    class Meta:
        app_label = "core"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"