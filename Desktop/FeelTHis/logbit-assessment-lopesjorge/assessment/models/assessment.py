
from configuracao_assessment.models import ConfiguracaoAssessment
from crum import get_current_user
from curso.models import Modulo
from django.contrib.auth.models import User
from django.db import models


class Assessment(models.Model):
    """
       Classe Assessment implementa as funções relacionadas aos assessments
    """

    nome = models.CharField(
        max_length=250,
        verbose_name="Nome",
        help_text="Campo Obrigatório"
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True, null=True
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Usuário"
    )

    configuracao_assessment = models.ForeignKey(
        ConfiguracaoAssessment,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Configuração Assessment"
    )
    
    modulo = models.ForeignKey(
        Modulo,
        verbose_name='Módulo',
        help_text='Módulo ao qual o assessment pertence',
        blank=True, null=True,
        on_delete=models.CASCADE
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
        super(Assessment, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "assessment"
        verbose_name = "Assessment"
        verbose_name_plural = "Assessments"
