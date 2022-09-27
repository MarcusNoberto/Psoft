from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from respostas.models import Resposta
from curso.models import Curso, RegistroCapitulo
from dateutil.relativedelta import relativedelta
from datetime import datetime

@login_required
def curso(request, id_curso, slug_projeto):
    curso = get_object_or_404(Curso, id=id_curso)
    modulos = curso.modulo_set.all()
    perguntas_com_respostas =[]
    for modulo in modulos:
        resposta =[]
        quantidade_resposta=0
        for pergunta in modulo.get_perguntas():
            quantidade_resposta+=len(
                Resposta.objects.filter(
                    usuario=request.user, 
                    pergunta_multipla_escolha=pergunta
                )
            )
            
        perguntas_com_respostas.append(
            {
                "titulo": modulo.titulo,
                "quantidade_respostas": quantidade_resposta,
                "quantidade_perguntas": len(modulo.get_perguntas()),
                "score": round((quantidade_resposta/(len(modulo.get_perguntas()) or 1) * 100), 2)
            }
        )

    lista_progresso_videosaulas = RegistroCapitulo.objects.filter(
        modulo=curso, 
        usuario=request.user, 
        tipo='Progresso nas Videoaulas'
    ).order_by('data_hora')

    
    lista_progresso_perguntas = RegistroCapitulo.objects.filter(
        modulo=curso, 
        usuario=request.user, 
        tipo='Progresso no Quizz'
    ).order_by('data_hora')

    data_time_atual = datetime.today()
    primeiro_registro_videos = lista_progresso_videosaulas.first().data_hora if lista_progresso_videosaulas.exists() else data_time_atual
    ultimo_registro_videos = lista_progresso_videosaulas.last().data_hora if lista_progresso_videosaulas.exists() else data_time_atual
    primeiro_registro_quizz = lista_progresso_perguntas.first().data_hora if lista_progresso_perguntas.exists() else data_time_atual
    ultimo_registro_quizz = lista_progresso_perguntas.last().data_hora if lista_progresso_perguntas.exists() else data_time_atual

    data_base_video = primeiro_registro_videos
    data_base_quizz = primeiro_registro_quizz

    listagem_quizz_registros =[]
    cache_ultimo_progresso = 0
    while data_base_quizz <= ultimo_registro_quizz:
        registro_atual = lista_progresso_perguntas.filter(data_hora__month=data_base_quizz.month, data_hora__year=data_base_quizz.year).last()

        if registro_atual and registro_atual.data_hora.month == data_time_atual.month and registro_atual.data_hora.year == data_time_atual.year:
            progresso = curso.progresso_quizz
        else:
            progresso = registro_atual.progresso if registro_atual else cache_ultimo_progresso

        if progresso > 0:
            cache_ultimo_progresso = progresso

        listagem_quizz_registros.append(
            {
                "data": data_base_quizz,
                "progresso": round(float(progresso), 2)
            }
        )
        data_base_quizz=data_base_quizz+relativedelta(months=1)

    listagem_videos_registros =[]
    cache_ultimo_progresso = 0
    while data_base_video <= ultimo_registro_videos:
        registro_atual = lista_progresso_videosaulas.filter(data_hora__month=data_base_video.month, data_hora__year=data_base_video.year).last()
    
        if registro_atual and registro_atual.data_hora.month == data_time_atual.month and registro_atual.data_hora.year == data_time_atual.year:
            progresso = curso.progresso_video
        else:
            progresso = registro_atual.progresso if registro_atual else cache_ultimo_progresso

        if progresso > 0:
            cache_ultimo_progresso = progresso

        listagem_videos_registros.append(
            {
                "data": data_base_video,
                "progresso": round(float(progresso), 2)
            }
        )
        data_base_video+=relativedelta(months=1)


    quantidade_modulos = modulos.count()
    quantidade_modulos_concluidos = 0
    quantidade_aulas = 0
    quantidade_aulas_concluidas = 0

    for modulo in modulos:
        quantidade_modulos_concluidos +=  1 if modulo.modulo_concluido else 0
        quantidade_aulas += len(modulo.video_set.all())
        quantidade_aulas_concluidas += modulo.total_videos_finalizados

    next_aulas = []
    usuario_novo = False
    usuario_normal = False
    usuario_completo = True
    if RegistroCapitulo.objects.filter(usuario=request.user).exists():
        usuario_normal = True
    else:
        usuario_novo = True
    for modulo in modulos:
        for video in modulo.videos_desse_modulo().lista_videos:
            if not request.user in video.usuarios_concluintes.all():
                next_aulas.append(video)
            if request.user not in video.usuarios_concluintes.all():
                usuario_completo= False
    next_aula = None
    for modulo in modulos:
        for video in modulo.videos_desse_modulo().lista_videos:
            if not request.user in video.usuarios_concluintes.all():
                next_aula = video
                break
            


    usuario_novo = True

    modulos_certos = []
    for modulo in curso.progresso_curso().lista_modulos:
        modulos_certos.append(modulo.primeiro_video_do_modulo)
    
    percentual_aulas = (quantidade_aulas_concluidas/quantidade_aulas) *100 if quantidade_aulas else 1
    ultimo_registro_com_video = RegistroCapitulo.objects.filter(
        modulo = curso,
        video__isnull=False,
        usuario=request.user, 
        tipo='Progresso nas Videoaulas'
    ).order_by('data_hora').last()
    if request.user not in curso.usuarios_com_acesso.all() or not curso.atingiu_pre_requisito:
        return HttpResponseForbidden()
    
    
    
    
    else:
        context = {
            'curso': curso,
            'title': curso.titulo,
            'percentual_aulas': percentual_aulas,
            'modulos': modulos,
            'quantidade_aulas': quantidade_aulas,
            'quantidade_aulas_concluidas': quantidade_aulas_concluidas,
            'quantidade_modulos': quantidade_modulos,
            'quantidade_modulos_concluidos': quantidade_modulos_concluidos,
            'perguntas_com_respostas': perguntas_com_respostas,
            'listagem_quizz_registros': listagem_quizz_registros,
            'listagem_videos_registros': listagem_videos_registros,
            'tamanho_listagem_videos_registros': len(listagem_videos_registros),
            'tamanho_listagem_quizz_registros': len(listagem_quizz_registros),
            'progresso_restante_video': round(100 - curso.progresso_video, 2) if curso else None,
            'ultimo_registro_com_video': ultimo_registro_com_video,
            'next_aulas': next_aulas,
            'usuario_normal' : usuario_normal,
            'next_aula': next_aula if next_aula else curso.primeiro_video_modulo,
            'usuario_novo' : usuario_novo,
            'usuario_completo' : usuario_completo,
            'modulos_certos' : modulos_certos
        }

        return render(
            request,
            'curso/curso.html',
            context
        )
