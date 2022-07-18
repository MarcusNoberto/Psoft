from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404

from curso.models import Avaliacao, Video


@login_required
def avaliar_video(request):
    if request.method != 'POST':
        return HttpResponseForbidden()

    video_id = request.POST.get('video_id', None)
    video = get_object_or_404(Video, id=video_id)
    nota = request.POST.get('nota', None)

    avaliacao = Avaliacao.objects.filter(
        video=video,
        usuario_criacao=request.user
    ).first()

    if avaliacao:
        avaliacao.update_nota(nota)
    else:
        Avaliacao.objects.create(
            video=video,
            nota=nota
        )

    return JsonResponse({'status': 'success'})
