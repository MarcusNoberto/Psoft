from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Anexo
from .item_anexo_inline import ItemAnexoInline


# @admin.register(Anexo)
class AnexoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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

    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'data_criacao',
        'data_alteracao',
    ]
    
    
    fieldsets = [
        ('Dados Principais', {'fields': (
			'titulo',
			'descricao',
		)}),
        ('Configuração Principal', {'fields':(
            'assessment',
        )}),
        ('Configuração de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    ]

    inlines = [
        ItemAnexoInline,
    ]
