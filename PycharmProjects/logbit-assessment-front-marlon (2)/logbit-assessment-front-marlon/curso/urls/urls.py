from django.urls import include, path

from ..views import avaliacao
from ..views.comentario import url_criar_comentario
from ..views.curso_views import conclusao_curso, conclusao_modulo, curso
from .video_urls import video_urls

urlpatterns = [
    path('<int:id_curso>/', curso, name='curso'),
    path('conclusao_modulo/<int:id_modulo>/', conclusao_modulo, name='conclusao_modulo'),
    path('conclusao_curso/<int:id_curso>/', conclusao_curso, name='conclusao_curso'),

    path('avaliacao/<int:id_avaliacao>/<str:tipo_pergunta>/<int:id_pergunta>/', avaliacao, name='avaliacao'),
    path('url_criar_comentario/', url_criar_comentario, name='url_criar_comentario'),
    path('video/', include(video_urls, namespace='video')),
]
