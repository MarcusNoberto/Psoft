from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import AnexoVideo


@admin.register(AnexoVideo)
class AnexoVideoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'titulo',
        'video',
        'anexo',
    ]

    autocomplete_fields = [
        'video',
    ]

    search_fields = [
        'titulo',
        'id',
        'video',
        'anexo',
    ]

    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'data_criacao',
        'data_alteracao',
    ]

    fieldsets = [
        ('Dados principais', {'fields': [
            'titulo',
            'anexo',
            'video',
        ]}),
        ('Dados complementares', {'fields': [
            'usuario_criacao',
            'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
        ]})
    ]
