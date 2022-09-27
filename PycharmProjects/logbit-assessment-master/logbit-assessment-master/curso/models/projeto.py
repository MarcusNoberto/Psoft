from django.db import models
from crum import get_current_user

class Projeto(models.Model):
    

    titulo = models.CharField(
        max_length=250,
        verbose_name="Título",
        help_text="Campo Obrigatório"
    )

    slug = models.SlugField(
        max_length=250,
        verbose_name="Slug",
        help_text="Campo Obrigatório"
    )
    

    CHOICES_LINGUAGEM = [
        ('PT', 'PT'),
        ('ES', 'ES'),
        ('EN', 'EN')
    ]

    linguagem = models.CharField(
        verbose_name='Linguagem',
        max_length=7,
        choices=CHOICES_LINGUAGEM,
        default='PT'
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        null=True, blank=True
    )

    foto_capa = models.ImageField(
        verbose_name='Foto de capa',
        help_text = 'Resolução sugerida 320 x 450',
        blank=True, null=True
    )

    usuarios_com_acesso = models.ManyToManyField(
		'auth.User', 
        verbose_name=('Usuários com acesso'),
        blank=True,
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

    class Meta:
        app_label = 'curso'
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
