import nested_admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import PerguntaMultiplaEscolha
from .alternativa_multipla_escolha_inline import AlternativaMultiplaEscolhaInline


@admin.register(PerguntaMultiplaEscolha)
class PerguntaMultiplaEscolhaAdmin(ImportExportModelAdmin, nested_admin.NestedModelAdmin):
    list_display = [
        'id',
        'titulo',
        'valor_minimo',
        'modulo',
        'curso',
    ]

    search_fields = [
        'id',
        'titulo',
        'valor_minimo',
        'modulo__titulo',
    ]

    autocomplete_fields = [
        'modulo',
    ]

    fieldsets = [
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
            'valor_minimo'
		)}),
        ('Configurações', {'fields': (
            'modulo',
            'ordem',
            'contem_mais_de_uma_resposta',
        )})
    ]

    inlines = [
        AlternativaMultiplaEscolhaInline,
    ]
