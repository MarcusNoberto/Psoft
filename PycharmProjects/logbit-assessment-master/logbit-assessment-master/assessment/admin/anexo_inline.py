import nested_admin

from ..models import Anexo
from .item_anexo_inline import ItemAnexoInline


class AnexoInline(nested_admin.NestedTabularInline):
    model = Anexo

    extra = 0

    fieldsets = [
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
		)}),
        ('Configuração Principal', {'fields':(
            'assessment',
        )}),
    ]

    inlines = [
        ItemAnexoInline,
    ]
