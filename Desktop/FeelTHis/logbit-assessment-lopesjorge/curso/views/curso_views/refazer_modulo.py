from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy

from curso.models import Modulo


@login_required
def refazer_modulo(request, id_modulo):
    modulo = Modulo.objects.get(id=id_modulo)
    modulo.reinicia_usuario_perguntas
    args = {
        'tipo_pergunta' : 'pergunta_multipla_escolha',
        'pergunta_id' : modulo.primeira_pergunta
    }
    return redirect(reverse_lazy('responder_pergunta', kwargs = args))