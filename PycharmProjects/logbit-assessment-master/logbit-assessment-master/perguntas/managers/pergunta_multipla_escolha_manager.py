#Shift + Alt + O para organizar as importações (vs code)

from django.db import models
from django.db.models import F, Sum


class PerguntaMultiplaEscolhaManager(models.Manager):
    '''
    Classe destinada para implementar as funcionalidades
    referentes à várias perguntas de múltipla escolha.
    '''

    def nota_maxima_perguntas(query:list) -> float:
        '''
        Função que recebe uma lista (query na verdade) de perguntas
        e retorna a nota máxima que todas essas perguntas poderiam ter.
        '''

        return sum(pergunta.nota_maxima for pergunta in query.all())
