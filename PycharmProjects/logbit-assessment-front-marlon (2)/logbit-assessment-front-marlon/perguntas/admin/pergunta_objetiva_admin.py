import nested_admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import PerguntaObjetiva
from .alternativa_objetiva_inline import AlternativaObjetivaInline


# @admin.register(PerguntaObjetiva)
class PerguntaObjetivaAdmin(ImportExportModelAdmin, nested_admin.NestedModelAdmin):
    list_display = [
        'id',
        'titulo',
    ]

    search_fields = [
        'id',
        'titulo',
    ]

    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'data_criacao',
        'data_atualizacao',
    ]

    autocomplete_fields = [
        'modulo',
        'alternativa_correta',
    ]

    fieldsets = [
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
		)}),
        ('Configurações', {'fields':(
            'modulo',
            'ordem',
            'alternativa_correta',
        )}),
    ]

    inlines = [
        AlternativaObjetivaInline,
    ]
