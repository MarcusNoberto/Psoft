from django import template

from decouple import config
PRODUCAO = config('PRODUCAO', default=True, cast=bool)

register = template.Library()
from core.models import Instrucao

@register.simple_tag
def video_instrucao(request):
    from core.models import Fabricante

    if PRODUCAO:
        nome_fabricante = request.session['dados_usuario']['fabricanteName']
        fabricante = Fabricante.objects.get(nome_auth=nome_fabricante)
    else:
        fabricante = Fabricante.objects.get(nome_auth="TESTE")

    linguagem = fabricante.linguagem

    try:
        return Instrucao.objects.filter(linguagem=linguagem).first().video.url
    except:
        return None