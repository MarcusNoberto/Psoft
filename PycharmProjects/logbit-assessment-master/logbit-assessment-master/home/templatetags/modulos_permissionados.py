from core.models import Fabricante
from curso.models import Curso, Projeto
from decouple import config
import json
PRODUCAO = config('PRODUCAO', default=True, cast=bool)

from django import template


register = template.Library()

@register.simple_tag
def modulos_p(request):
    slug = 'teste'
    if 'video' in request.path_info:
        slug = request.path_info.split('/')[5]
    elif 'conclusao_modulo' in request.path_info:
        slug = request.path_info.split('/')[4]
    elif 'responder' in request.path_info:
        slug = request.path_info.split('/')[5]
    elif 'cursos' in request.path_info:
        slug = request.path_info.split('/')[3]
    else:
        slug = request.path_info.split('/')[1]
    if PRODUCAO:
        nome_fabricante = request.session['dados_usuario']['fabricanteName']
        fabricante = Fabricante.objects.get(nome_auth=nome_fabricante)
    else:
        fabricante = Fabricante.objects.get(nome_auth="TESTE")


    projeto = Projeto.objects.filter(slug = slug).first()

    modulos = Curso.objects.filter(linguagem=fabricante.linguagem, projeto = projeto).distinct()
    return modulos