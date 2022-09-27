from unicodedata import name
from django import template

register = template.Library()

@register.filter(name='vezes')
def vezes(number: float) -> range:
    '''
    Filtro simples, usado para percorrer o tamanho de alguma coisa.
    Recebemos o tamanho de alguma coisa e retornamos um range com isso.

    Por isso o nome vezes, vamos fazer alguma coisa tantas vezes.
    '''
    return range(int(number))
