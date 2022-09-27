from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'nota',
    ]

    search_fields = [
        'id',
        'nota',
    ]

    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'data_criacao',
        'data_alteracao',
    ]

    autocomplete_fields = [
        'video',
    ]

    fieldsets = (
        ('Dados Principais', {'fields': (
			'nota',
            'feedback',
            'video',
		)}),
        ('Dados de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    )
