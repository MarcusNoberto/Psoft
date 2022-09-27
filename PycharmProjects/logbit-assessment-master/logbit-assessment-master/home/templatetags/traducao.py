from django import template

register = template.Library()
from decouple import config
PRODUCAO = config('PRODUCAO', default=True, cast=bool)


@register.simple_tag
def traduzir(palavra, request):
    from core.models import Fabricante
    from core.models import Traducao
    if PRODUCAO:
        nome_fabricante = request.session['dados_usuario']['fabricanteName']
        fabricante = Fabricante.objects.get(nome_auth=nome_fabricante)
    else:
        fabricante = Fabricante.objects.get(nome_auth="TESTE")
    linguagem = fabricante.linguagem
    
    try:
        traducao = Traducao.objects.get(portugues__iexact=palavra)
        
        if linguagem == 'PT':
            if traducao.portugues:
                return traducao.portugues
        elif linguagem == 'ES':
            if traducao.espanhol:
                return traducao.espanhol
        elif linguagem=='EN':
            if traducao.ingles:
                return traducao.ingles
                
        return palavra
    except:
        return palavra
