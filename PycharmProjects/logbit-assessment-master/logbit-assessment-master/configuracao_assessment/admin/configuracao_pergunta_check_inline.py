import nested_admin

from ..models import ConfiguracaoPerguntaCheck


class ConfiguracaoPerguntaCheckInline(nested_admin.NestedTabularInline):
    model = ConfiguracaoPerguntaCheck
    
    extra = 0
    
    fieldsets = (
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
		)}),
        ('Configuração Principal', {'fields':(
            'resposta_esperada',
            
        )}),
    )
