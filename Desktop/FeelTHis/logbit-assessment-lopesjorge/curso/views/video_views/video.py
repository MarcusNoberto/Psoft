from curso.models import AnexoVideo, Avaliacao, Modulo, Video, Curso
from django.db.models import Avg
from django.http import HttpResponseForbidden
from django.shortcuts import render


def video(request, id_modulo, id_video, slug_projeto):
    modulo_atual = Modulo.objects.get(id=id_modulo)
    if modulo_atual.class_sidebar == 'disabled':
        return HttpResponseForbidden()
    curso_atual = curso = Curso.objects.filter(modulo = modulo_atual).first()

    proximo_video_nao_concluido = None
    video_atual = Video.objects.get(id=id_video)

    videos = Video.objects.filter(modulo=id_modulo).order_by('ordem', 'id').distinct()
    id_videos = []
    videos_nao_concluidos=[]
    for video in videos:
        id_videos.append(video.id)
        if not request.user in video.usuarios_concluintes.all():
            videos_nao_concluidos.append(video.id)
    for video in videos:
        if not request.user in video.usuarios_concluintes.all():
            if video != video_atual:
                proximo_video_nao_concluido = video
                break
    

    
        
    id_proximo = -1
    id_anterior = -1
    for index, id_video in enumerate(id_videos) :
        if video_atual.id == id_video:
            id_proximo = index +1
            id_anterior = index -1
    video_proximo = None
    video_anterior = None
    try:
        video_proximo = videos[id_proximo]
    except:
        pass
    try:
        video_anterior = videos[id_anterior]
    except:
        pass
    concluiu_todas = False
    if (modulo_atual.videos_desse_modulo().total_videos - modulo_atual.videos_desse_modulo().quantidade_videos_concluidos) == 0:
        concluiu_todas = True
    else:
        concluiu_todas  = False
            

    anexos = AnexoVideo.objects.filter(video=id_video)

    avaliacoes = Avaliacao.objects.filter(video=id_video)

    comentarios = video_atual.comentario_set.filter(
        resposta_comentario__isnull=True
    )

    media_avaliacoes = avaliacoes.aggregate(Avg('nota'))['nota__avg'] or None
    estrelas_preenchidas = int(media_avaliacoes) if media_avaliacoes else 0
    estrelas = config_estrelas(estrelas_preenchidas)

    context = {
        'videos':videos,
        'video_atual':video_atual,
        'video_proximo': video_proximo,
        'video_anterior': video_anterior,

        'modulo_atual':modulo_atual,

        'avaliacoes':avaliacoes,
        'proximo_video_nao_concluido': proximo_video_nao_concluido if proximo_video_nao_concluido else None,

        'comentarios':comentarios,

        'anexos':anexos,
        'concluiu_todas' : concluiu_todas,

        'estrelas':estrelas,

        'title': video_atual.titulo,
        'curso_atual' : curso_atual,
        'videos_nao_concluidos': videos_nao_concluidos,
        'quantidade_videos_nao_concluidos': len(videos_nao_concluidos)
    }

    return render(
        request,
        'video_templates/video.html',
        context
    )

#ANCHOR funções auxiliares
def config_estrelas(estrelas_preenchidas: int) -> list:
    '''
    Função que recebe o número de estrelas preenchidas
    e retorna uma lista contendo o id e se a estrela
    está preenchida ou não.
    '''

    return [{
        'data_star': i+1,
        'preenchida': i+1 <= estrelas_preenchidas # Até o número de estrelas preenchidas setamos True, depois False
    } for i in range(0, 5)]
