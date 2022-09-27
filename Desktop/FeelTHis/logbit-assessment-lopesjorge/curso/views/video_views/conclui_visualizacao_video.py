from curso.models import Video
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from funcoes_utilitarias.redirect import redirect_next_item_config
from curso.models import RegistroCapitulo
from datetime import datetime
def conclui_visualizacao_video(request):
    video = get_object_or_404(Video, pk=request.POST.get('video_id'))
    video.conclui_visualizacao(request.user)
    # atualização no progresso do capitulo
    modulo=video.modulo.curso
    RegistroCapitulo.objects.create(
        modulo=modulo,
        usuario=request.user,
        data_hora=datetime.today(),
        progresso=modulo.progresso_video,
        video=video
    )

    profile = request.user.profile

    if profile:
        profile.atualiza_ultima_aula(video)

    return JsonResponse({'url': redirect_next_item_config(video)})
