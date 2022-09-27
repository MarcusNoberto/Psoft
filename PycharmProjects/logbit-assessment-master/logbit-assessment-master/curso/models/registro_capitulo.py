from django.db import models
from django.contrib.auth.models import User
from curso.models import Curso
from curso.models import Video

class RegistroCapitulo(models.Model):
    '''
    A classe RegistroModulo serve para armazernar os(as) registros do módulo do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo RegistroModulo.
    '''
    CHOICE_TIPO = (
        ('Progresso nas Videoaulas', 'Progresso nas Videoaulas'),
        ('Progresso no Quizz', 'Progresso no Quizz')
    )
    tipo = models.CharField(
        verbose_name="Tipo de Registro",
        max_length=100,
        choices=CHOICE_TIPO,
        default="Progresso nas Videoaulas",
        null=True
    )
    
    usuario = models.ForeignKey(
        User,
        verbose_name='Usuário',
        on_delete=models.SET_NULL,
        null=True
    )

    data_hora = models.DateTimeField(
        verbose_name="Data e Hora",

    )

    modulo = models.ForeignKey(
        Curso,
        verbose_name="Modulo",
        on_delete=models.SET_NULL,
        null=True
    )

    progresso = models.DecimalField(
        verbose_name="Progresso no Capitulo",
        default=0,
        decimal_places=2,
        max_digits=10
    )
    
    video = models.ForeignKey(
        Video,
        verbose_name="Videoaula",
        on_delete=models.SET_NULL,
        null=True,
        blank=True

    )

    def __str__(self):
        return f'{self.id} - {self.tipo}'

    class Meta:
        app_label = 'curso'
        verbose_name = 'Registro do Capitulo'
        verbose_name_plural = 'Registros dos Capitulos'
