from crum import get_current_user
from django.db import models

from assessment.models.assessment import Assessment


class PerguntaDiscursiva(models.Model):
    """
        Classe PerguntaDiscursiva implementa as funções relacionadas as perguntas discursivas
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

    resposta = models.TextField(
        verbose_name="Resposta",
        null=True, blank=True
    )

    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Assessment"
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

    usuarios_responderam = models.ManyToManyField(
        'auth.User',
        verbose_name='Usuários que responderam',
        blank=True
    )

    def __str__(self):
       return self.titulo
    
    def marcar_respondida(self, usuario):
        self.usuarios_responderam.add(usuario)
        self.save()

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(PerguntaDiscursiva, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "assessment"
        verbose_name = "Pergunta Discursiva"
        verbose_name_plural = "Perguntas Discursivas"
