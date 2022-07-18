import nested_admin

from ..models import ConfiguracaoAnexo


class ConfiguracaoAnexoInline(nested_admin.NestedTabularInline):
    model = ConfiguracaoAnexo

    extra = 0

    fieldsets = (
      ('Dados Principais', {'fields': (
        'titulo',
        'descricao',
      )}),
    )
