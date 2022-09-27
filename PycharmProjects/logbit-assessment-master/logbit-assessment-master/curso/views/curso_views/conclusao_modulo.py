from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from curso.models import Modulo
from curso.models import Curso


@login_required
def conclusao_modulo(request, id_modulo, slug_projeto):
    modulo = Modulo.objects.get(id=id_modulo)
    curso = Curso.objects.filter(modulo = modulo).first()
    next = False
    next_modulo = None
    ultimo_curso = False
    next_video = None
    encontrou = False
    for modulo_n in curso.modulo_set.filter().exclude(id=modulo.id):
        for video in modulo_n.video_set.all():
            if not request.user in video.usuarios_concluintes.all() and not encontrou:
                next_video = video
                encontrou = True
                
            
    for modulo_atual in curso.progresso_curso().lista_modulos:
        next_modulo = modulo_atual
        if next == True:
            break
        if modulo_atual.titulo == modulo.titulo:
            next = True
    next_curso = None
    continua_curso = True
    if curso.ultimo_modulo == modulo:
        continua_curso = False
        next = False
        for curso_atual in Curso.objects.all():
            next_curso = curso_atual
            if next == True:
                break
            if curso_atual == curso:
                next = True

    if curso.titulo == Curso.objects.all().last().titulo:
        ultimo_curso = True
        



    
    
    lista_aulas = next_modulo.videos_desse_modulo().lista_videos

    total_perguntas = len(modulo.get_perguntas())
    quantos_acertos = len(modulo.perguntas_certas())
    percent_acertos = (quantos_acertos/total_perguntas) * 100
    medalha = 'Bronze'

    if percent_acertos >= curso.pontuacao_ouro:
        medalha = 'Ouro'
    elif percent_acertos >= curso.pontuacao_prata:
        medalha = 'Prata'
        
    context = {
        'title': modulo.titulo,
        'modulo': modulo,
        'curso': curso,
        'total_perguntas': total_perguntas,
        'quantos_acertos': quantos_acertos,
        'percent_acertos': round(percent_acertos, 2),
        'medalha': medalha,
        'lista_proximas_aulas' : lista_aulas if lista_aulas else None,
        'next_modulo' : next_modulo,
        'next_video': next_video,
        'page_is_capitulo_conclusao': True,
        'continua_curso' : continua_curso,
        'next_curso' : next_curso,
        'ultimo_curso' : ultimo_curso

    }

    return render(
        request,
        'curso/conclusoes/conclusao_modulo.html',
        context
    )
