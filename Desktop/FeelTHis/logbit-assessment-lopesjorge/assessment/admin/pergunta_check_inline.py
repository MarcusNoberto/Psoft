import nested_admin

from ..models import PerguntaCheck


class PerguntaCheckInline(nested_admin.NestedTabularInline):
    model = PerguntaCheck

    extra = 0

    fieldsets = [
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
		)}),
        ('Configuração Principal', {'fields':(
            'resposta_esperada',
            'resposta',
            'assessment'
        )}),
    ]
