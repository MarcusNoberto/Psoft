#Shift + Alt + O para organizar as importações (vs code)

from django.db import models
from django.db.models import Sum


class RespostaManager(models.Manager):
    '''
    Classe destinada para implementar as funcionalidades
    referentes à várias respostas.
    '''

    def pontuacao_usuario(query: list, usuario: object, modulo=None, curso=None) -> float:
        '''
        Função para retornar a pontuação total de um usuário
        em um módulo ou um curso
        '''
        if modulo:
            query = query.filter(
                usuario=usuario,
                pergunta_multipla_escolha__modulo=modulo
            )
            return query.aggregate(
                total=Sum(
                    'pontuacao'
                )
            )['total'] or 0
        elif curso:
            query = query.filter(
                usuario=usuario,
                pergunta_multipla_escolha__modulo__curso=curso
            )
            return query.aggregate(
                total=Sum(
                    'pontuacao'
                )
            )['total'] or 0
        
        return -1
