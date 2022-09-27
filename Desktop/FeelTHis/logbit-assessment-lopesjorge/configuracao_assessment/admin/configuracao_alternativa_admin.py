from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import ConfiguracaoAlternativa


# @admin.register(ConfiguracaoAlternativa)
class ConfiguracaoAlternativaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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
            'configuracao_pergunta_objetiva',
        )}),
        ('Configuração de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    )
