from django.db import models


class ModuloManager(models.Manager):
    '''
    Classe para implementar as funcionalidades relacionadas a vários módulos.
    '''

    def total_modulos_concluidos(query):
        '''
        Função que diz a quantidade de módulos concluídos, exemplos de chamadas:

        curso.modulo_set.total_modulos_concluidos()
        Modulo.objects.filter(curso=my_curse).total_modulos_concluidos()
        Modulo.objects.total_modulos_concluidos()
        '''
        return len(list(
            filter(lambda modulo: modulo.modulo_concluido, query.all())
        ))
    
    def nota_maxima_modulos(query):
        return sum(modulo.pontuacao_maxima for modulo in query.all())
