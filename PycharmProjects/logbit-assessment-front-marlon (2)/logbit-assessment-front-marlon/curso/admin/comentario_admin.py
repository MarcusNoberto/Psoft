from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'comentario',
        'video',
        'usuario_criacao',
    ]

    search_fields = [
        'id',
        'comentario',
        'video__titulo',
        'usuario_criacao__username',
    ]

    list_filter = [
        'usuario_criacao',
        'data_criacao',
    ]

    autocomplete_fields = [
        'video',
        'resposta_comentario',
    ]

    exclude = [
        'usuario_criacao',
        'usuario_atualizacao',
    ]
