from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import ConfiguracaoPerguntaDiscursiva


# @admin.register(ConfiguracaoPerguntaDiscursiva)
class ConfiguracaoPerguntaDiscursivaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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
            
        )}),
        ('Configuração de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    )
