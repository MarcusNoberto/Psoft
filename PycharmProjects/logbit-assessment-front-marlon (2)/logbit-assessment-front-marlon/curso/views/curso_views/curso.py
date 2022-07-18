from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render

from curso.models import Curso


@login_required
def curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)
    
    if request.user not in curso.usuarios_com_acesso.all() or not curso.atingiu_pre_requisito:
        return HttpResponseForbidden()
    
    else:
        context = {
            'curso': curso,
            'title': curso.titulo
        }

        return render(
            request,
            'curso/curso.html',
            context
        )
