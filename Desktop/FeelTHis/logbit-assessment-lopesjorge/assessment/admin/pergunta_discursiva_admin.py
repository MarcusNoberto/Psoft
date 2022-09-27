import nested_admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import PerguntaDiscursiva


# @admin.register(PerguntaDiscursiva)
class PerguntaDiscursivaAdmin(ImportExportModelAdmin, nested_admin.NestedModelAdmin):
    list_display = [
        'id',
        'titulo',
        'assessment',
    ]

    search_fields = [
        'id',
        'titulo',
        'assessment',
    ]

    autocomplete_fields = [
        'assessment',
    ]

    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'usuarios_responderam',
        'data_criacao',
        'data_alteracao',
    ]

    fieldsets = [
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
		)}),
        ('Configuração Principal', {'fields':(
            'resposta',
            'assessment',
        )}),
        ('Configuração de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'usuarios_responderam',
            'data_criacao',
            'data_alteracao',
		)}),
    ]
