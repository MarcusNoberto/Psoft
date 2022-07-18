from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import ConfiguracaoPerguntaCheck


# @admin.register(ConfiguracaoPerguntaCheck)
class ConfiguracaoPerguntaCheckAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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
            'resposta_esperada',
            
        )}),
        ('Configuração de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    )
