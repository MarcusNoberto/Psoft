import nested_admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .configuracao_alternativa_inline import ConfiguracaoAlternativaInline

from ..models import ConfiguracaoPerguntaObjetiva


# @admin.register(ConfiguracaoPerguntaObjetiva)
class ConfiguracaoPerguntaObjetivaAdmin(ImportExportModelAdmin, nested_admin.NestedModelAdmin):
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
        'data_alteracao',
    ]

    fieldsets = (
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
		)}),
        ('Configuração Principal', {'fields':(
            'alternativa_correta',
            
        )}),
        ('Configuração de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    )

    inlines = [
        ConfiguracaoAlternativaInline,
    ]
