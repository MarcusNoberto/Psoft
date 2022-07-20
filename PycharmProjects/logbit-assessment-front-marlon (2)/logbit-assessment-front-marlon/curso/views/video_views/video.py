from curso.models import AnexoVideo, Avaliacao, Modulo, Video
from django.db.models import Avg
from django.http import HttpResponseForbidden
from django.shortcuts import render


def video(request, id_modulo, id_video):
    modulo_atual = Modulo.objects.get(id=id_modulo)
    if modulo_atual.class_sidebar == 'disabled':
        return HttpResponseForbidden()

    video_atual = Video.objects.get(id=id_video)

    videos = Video.objects.filter(modulo=id_modulo).order_by('ordem', 'id')
    id_videos = []
    for id in videos:
        id_videos.append(id.id)
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

        'comentarios':comentarios,

        'anexos':anexos,

        'estrelas':estrelas,

        'title': video_atual.titulo
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
