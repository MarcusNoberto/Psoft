from django.db import models
from crum import get_current_user

class ConfiguracaoAlternativa(models.Model):
    """
        Classe ConfiguracaoAlternativa implementa as funções relacionadas as configuracões das alternativas
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

    configuracao_pergunta_objetiva = models.ForeignKey(
        'configuracao_assessment.ConfiguracaoPerguntaObjetiva',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Configuração pergunta objetiva"
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
       return self.titulo

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(ConfiguracaoAlternativa, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "configuracao_assessment"
        verbose_name = "Configuração Alternativa"
        verbose_name_plural = "Configurações Alternativas"