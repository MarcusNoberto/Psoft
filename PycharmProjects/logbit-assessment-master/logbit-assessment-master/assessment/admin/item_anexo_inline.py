import nested_admin

from ..models import ItemAnexo


class ItemAnexoInline(nested_admin.NestedTabularInline):
    model = ItemAnexo

    extra = 0

    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'data_criacao',
        'data_alteracao',
    ]

    fieldsets = [
        ('Dados Principais', {'fields': (
			'arquivo',
			'anexo',
		)}),
    ]
