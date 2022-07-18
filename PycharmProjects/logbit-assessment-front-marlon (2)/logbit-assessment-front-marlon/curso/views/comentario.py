from ..models.comentario import Comentario
from ..models.video import Video
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from datetime import timedelta

@login_required
def url_criar_comentario(request):
    data = json.loads(request.body.decode("utf-8"))

    try:
        comentario = data['comentario']
    except:
        pass

    try:
        comentario_id=int(data['comentario_id'])
        resposta_comentario = Comentario.objects.get(id=comentario_id)
    except:
        resposta_comentario = None

    try:
        video_id = int(data['video_id'])
        video = Video.objects.get(id=video_id)

    except:
        video = None

    
    comentario = Comentario.objects.create(
        comentario=comentario,
        resposta_comentario=resposta_comentario,
        video=video
    )

    resposta={
        "id": comentario.id,
        "comentario": comentario.comentario,
        "first_name": comentario.usuario_criacao.first_name,
        "last_name": comentario.usuario_criacao.last_name,
        "username": comentario.usuario_criacao.username,
        "data_criacao": (comentario.data_criacao - timedelta(hours=3)).strftime("%d/%m/%Y")
    }


    return JsonResponse(resposta, safe=False)
