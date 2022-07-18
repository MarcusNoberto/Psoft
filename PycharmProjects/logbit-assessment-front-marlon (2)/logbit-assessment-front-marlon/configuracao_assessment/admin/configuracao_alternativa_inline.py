import nested_admin

from ..models import ConfiguracaoAlternativa


class ConfiguracaoAlternativaInline(nested_admin.NestedTabularInline):
    model = ConfiguracaoAlternativa
    
    extra = 0
    
    fieldsets = (
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
		)}),
        ('Configuração Principal', {'fields':(
            'configuracao_pergunta_objetiva',
        )}),
    )
