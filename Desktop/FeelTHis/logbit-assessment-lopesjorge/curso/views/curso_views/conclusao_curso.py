from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from curso.models import Modulo


@login_required
def conclusao_curso(request, id_curso, slug_projeto):
    curso = Modulo.objects.get(id=id_curso)
    context = {
        'curso': curso,
    }

    return render(
        request,
        'curso/conclusoes/conclusao_curso.html',
        context
    )
