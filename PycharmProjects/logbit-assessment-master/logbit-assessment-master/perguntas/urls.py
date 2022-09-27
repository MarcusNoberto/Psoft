#Shift + Alt + O para organizar as importações (vs code)

from django.urls import path

from .views import responder_pergunta

urlpatterns = [
    path('responder/<str:tipo_pergunta>/<int:pergunta_id>/<slug:slug_projeto>/', responder_pergunta, name='responder_pergunta'),
    path('responder/<str:tipo_pergunta>/<int:pergunta_id>/', responder_pergunta, name='responder_pergunta'),
]
