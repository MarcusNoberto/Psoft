from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from curso.models import Modulo


@login_required
def conclusao_modulo(request, id_modulo):
    modulo = Modulo.objects.get(id=id_modulo)

    total_perguntas = len(modulo.get_perguntas())
    quantos_acertos = len(modulo.perguntas_certas())
    percent_acertos = (quantos_acertos/total_perguntas) * 100
    medalha = 'Bronze'

    if percent_acertos >= 66.66:
        medalha = 'Ouro'
    elif percent_acertos >= 33.33:
        medalha = 'Prata'
        
    context = {
        'modulo': modulo,
        'total_perguntas': total_perguntas,
        'quantos_acertos': quantos_acertos,
        'percent_acertos': round(percent_acertos, 2),
        'medalha': medalha
    }

    return render(
        request,
        'curso/conclusoes/conclusao_modulo.html',
        context
    )
