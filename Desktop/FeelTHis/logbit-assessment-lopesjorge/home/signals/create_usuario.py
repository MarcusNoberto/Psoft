from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from curso.models import Curso



@receiver(post_save, sender=User)
def create_usuario(sender, instance, created, **kwargs):
    if created:
        cursos = Curso.objects.all()
        for curso in cursos:
            curso.usuarios_com_acesso.add(instance)
