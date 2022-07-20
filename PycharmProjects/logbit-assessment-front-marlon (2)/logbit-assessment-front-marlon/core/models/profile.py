from django.db import models
from django.contrib.auth.models import User
from curso.models import Video
from datetime import datetime
class Profile(models.Model):
    '''
    A classe Profile serve para armazernar os(as) nome da sua model do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Profile.
    '''
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )

    ultima_aula_vizualizada = models.ForeignKey(
        Video,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    data_ultima_aula = models.DateField()


    def atualiza_ultima_aula(self,video):
        self.ultima_aula_vizualizada = video
        self.data_ultima_aula = datetime.today()
        self.save()

    @property
    def usuario_novo(self):
        return self.ultima_aula_vizualizada == None

    def adiciona_acesso(self):
        self.acesso_set.create(profile = self)

    def acessos_mes(self, mes):
        return self.acesso_set.filter(data__month = mes).count()

    
    

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'core'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'