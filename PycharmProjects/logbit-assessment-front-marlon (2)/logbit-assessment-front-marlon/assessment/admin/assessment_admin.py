import nested_admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Assessment



# @admin.register(Assessment)
class AssessmentAdmin(ImportExportModelAdmin, nested_admin.NestedModelAdmin):
    list_display = [
        'id',
        'nome',
        # 'configuracao_assessment',
        'usuario',
    ]

    search_fields = [
        'id',
        'nome',
        'usuario__username'
    ]

    autocomplete_fields = [
        'usuario',
        # 'configuracao_assessment',
        'modulo',
    ]

    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'data_criacao',
        'data_alteracao'
    ]
    
    fieldsets = (
        ('Dados Principais', {'fields': (
			'nome',
			'descricao',
		)}),
        ('Configuração Principal', {'fields':(
            'usuario',
            # 'configuracao_assessment',
            'modulo',
        )}),
        ('Configuração de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    )
    
    #inlines = [
   #     EtapaNestedInline,
   # ]
#