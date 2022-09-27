#Shift + Alt + O para organizar as importações (vs code)

from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Resposta


@receiver(post_save, sender=Resposta)
def set_pontuacao(sender, instance, **kwargs):
    instance.set_pontuacao()
