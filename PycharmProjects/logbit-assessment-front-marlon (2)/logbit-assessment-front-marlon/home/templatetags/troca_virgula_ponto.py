from django import template

register = template.Library()

@register.simple_tag
def trocar_virgula_ponto(valor):
    str_valor = "{}".format(valor)
	
    valor = str_valor.replace(',', '.')

    return valor