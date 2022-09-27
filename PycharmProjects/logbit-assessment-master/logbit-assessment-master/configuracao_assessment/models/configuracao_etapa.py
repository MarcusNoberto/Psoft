from configuracao_assessment.models.configuracao_assessment import ConfiguracaoAssessment
from core.models.empresa import Empresa
from django.db import models
from crum import get_current_user

class ConfiguracaoEtapa(models.Model):
    """
       Classe ConfiguracaoEstapa implementa as funções relacionadas as configuracões das Etapas
    """

    nome = models.CharField(
        max_length=250,
        verbose_name="Nome",
        help_text="Campo Obrigatório"
    )

    ordem = models.IntegerField(
        verbose_name="Ordem",
        default=1,
		blank=True, null=True
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True, null=True
    )

    configuracao_assessment = models.ForeignKey(
        ConfiguracaoAssessment,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Configuração Assessment"
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

    def gerar_configuracoes(self):

        if self.grupos:
            for grupo in self.grupos.all():
                usuario_grupo = Group.objects.get(name=grupo).user_set.all()
                for usuario in usuario_grupo:
                    self.gerar_configuracoes_individual(usuario)

        for usuario in self.usuarios.all():
            self.gerar_configuracoes_individual(usuario)

    def gerar_configuracoes_individual(self, usuario):
        from assessment.models.assessment import Assessment

        configuracao = Assessment.objects.create(
                nome = self.nome,
                descricao = self.descricao,
                usuario = usuario,
                configuracao_assessment = self
            )

        return configuracao

    def __str__(self):
       return self.nome

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(ConfiguracaoEtapa, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "configuracao_assessment"
        verbose_name = "Configuração Etapa"
        verbose_name_plural = "Configurações Etapas"