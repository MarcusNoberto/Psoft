from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import PerguntaCheck


# @admin.register(PerguntaCheck)
class PerguntaCheckAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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
            'resposta_esperada',
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
