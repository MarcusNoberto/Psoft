from django.urls import path

from ..views import avaliar_video, conclui_visualizacao_video, video

video_urls = ([
    path('<int:id_modulo>/<int:id_video>/', video, name='video'),
    path('avaliar_video/', avaliar_video, name='avaliar_video'),
    path('conclui_visualizacao_video/', conclui_visualizacao_video, name='conclui_visualizacao_video'),
], 'video_urls')
