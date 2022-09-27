from django.urls import include, path

from ..views import avaliacao
from ..views.comentario import url_criar_comentario
from ..views.curso_views import conclusao_curso, conclusao_modulo, curso, refazer_modulo
from ..views.curso_views.projeto import projeto
from .video_urls import video_urls

urlpatterns = [
    path('<int:id_curso>/<slug:slug_projeto>/', curso, name='curso'),
    path('conclusao_modulo/<int:id_modulo>/<slug:slug_projeto>/', conclusao_modulo, name='conclusao_modulo'),
    path('conclusao_curso/<int:id_curso>/<slug:slug_projeto>/', conclusao_curso, name='conclusao_curso'),
    path('avaliacao/<int:id_avaliacao>/<str:tipo_pergunta>/<int:id_pergunta>/<slug:slug_projeto>/', avaliacao, name='avaliacao'),
    path('url_criar_comentario/', url_criar_comentario, name='url_criar_comentario'),
    path('refazer_quesao', refazer_modulo, name = 'refazer_questao'),
    path('video/', include(video_urls, namespace='video')),
]
