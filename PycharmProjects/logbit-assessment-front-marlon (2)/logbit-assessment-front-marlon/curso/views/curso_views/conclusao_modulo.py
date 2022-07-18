from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from curso.models import Modulo


@login_required
def conclusao_modulo(request, id_modulo):
    modulo = Modulo.objects.get(id=id_modulo)
    context = {
        'modulo': modulo,
    }

    return render(
        request,
        'curso/conclusoes/conclusao_modulo.html',
        context
    )
