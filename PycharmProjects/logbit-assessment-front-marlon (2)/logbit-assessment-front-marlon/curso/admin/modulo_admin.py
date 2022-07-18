import nested_admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from perguntas.admin import PerguntaMultiplaEscolhaInline

from ..models import Modulo
from .video_inline import VideoInline


@admin.register(Modulo)
class ModuloAdmin(ImportExportModelAdmin, nested_admin.NestedModelAdmin):
    list_display = [
        'id',
        'titulo',
        'curso',
    ]

    search_fields = [
        'id',
        'titulo',
        'curso__titulo',
    ]

    list_filter = [
        'curso',
    ]

    autocomplete_fields = [
        'curso',
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
            'curso',
            'ordem',
		)}),
        ('Dados de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    ]

    inlines = [
        VideoInline,
        PerguntaMultiplaEscolhaInline,
        # PerguntaObjetivaInline,
    ]
