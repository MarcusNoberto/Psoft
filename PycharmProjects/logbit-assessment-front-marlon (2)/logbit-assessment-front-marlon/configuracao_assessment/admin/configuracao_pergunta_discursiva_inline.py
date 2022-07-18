import nested_admin

from ..models import ConfiguracaoPerguntaDiscursiva


class ConfiguracaoPerguntaDiscursivaInline(nested_admin.NestedTabularInline):
    model = ConfiguracaoPerguntaDiscursiva
    
    extra = 0
    
    fieldsets = (
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
		)}),
    )
