import nested_admin

from ..models import PerguntaDiscursiva


class PerguntaDiscursivaInline(nested_admin.NestedTabularInline):
    model = PerguntaDiscursiva

    extra = 0

    fieldsets = [
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
		)}),
        ('Configuração Principal', {'fields':(
            'resposta',
            'assessment'
        )}),
    ]
