from django.db import models
from .profile import Profile

class Acesso(models.Model):
    '''
    A classe Acesso serve para armazernar os(as) nome da sua model do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Acesso.
    '''

    data = models.DateField(
        auto_now_add=True
        )
    profile = models.ForeignKey(
        Profile,
        on_delete= models.CASCADE,
    )

    class Meta:
        app_label = 'nome_app'
        verbose_name = 'Nome da sua model no singular'
        verbose_name_plural = 'Nome da sua model no plural'