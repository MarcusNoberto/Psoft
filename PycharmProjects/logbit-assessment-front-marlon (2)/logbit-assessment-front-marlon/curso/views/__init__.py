from .avaliacao import avaliacao
from .comentario import url_criar_comentario
from .curso_views import curso
from .video_views import avaliar_video, conclui_visualizacao_video, video

__all__ = [
    avaliacao,
    avaliar_video,
    conclui_visualizacao_video,
    curso,
    video,
    url_criar_comentario
]
