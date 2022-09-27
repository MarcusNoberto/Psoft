#Shift + Alt + O para organizar as importações (vs code)

from curso.models import Curso
from django import template
from django.shortcuts import get_object_or_404

from ..models import DicaOportunidade

register = template.Library()

@register.simple_tag()
def dicas_usuario(usuario: object, id_curso: int) -> list:
    '''
    Tag para retornar todas as dicas que
    precisam ser exibidas de um usuário.
    '''
    curso = get_object_or_404(Curso, id=id_curso)

    dicas_list = []
    respostas = usuario.resposta_set.all()
    for resposta in respostas:
        dicas_list.append(
            DicaOportunidade.objects.filter(
                pergunta_multipla_escolha__modulo__curso=curso,
                pergunta_multipla_escolha__valor_minimo__gt=resposta.pontuacao,
                pergunta_multipla_escolha=resposta.pergunta_multipla_escolha
            )
        )
    
    return set([dica for dica_list in dicas_list for dica in dica_list])
