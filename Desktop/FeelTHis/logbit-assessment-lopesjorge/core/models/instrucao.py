from django.db import models

class Instrucao(models.Model):
    '''
    A classe Instrucao serve para armazernar os(as) nome da sua model do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Instrucao.
    '''

    escolhas = (
        ('PT', 'PT'),
        ('EN', 'EN'),
        ('ES', 'ES')
    )

    video = models.FileField(
        verbose_name='Video',
        upload_to='video_instrucoes/',
        null=True,
    )
    
    linguagem = models.CharField(
        max_length = 100,
        choices = escolhas,
        default='PT'
    )

    def __str__(self):
        return self.linguagem

    class Meta:
        app_label = 'core'
        verbose_name = 'Instrucao'
        verbose_name_plural = 'Instrucoes'
