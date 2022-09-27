import nested_admin

from ..models import ConfiguracaoPerguntaObjetiva
from .configuracao_alternativa_inline import ConfiguracaoAlternativaInline


class ConfiguracaoPerguntaObjetivaInline(nested_admin.NestedTabularInline):
    model = ConfiguracaoPerguntaObjetiva

    extra = 0

    fieldsets = (
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
		)}),
        ('Configuração Principal', {'fields':(
            'alternativa_correta',
            
        )}),
    )

    inlines = [
        ConfiguracaoAlternativaInline,
    ]
