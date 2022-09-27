from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Video
from .anexo_video_inline import AnexoVideoInline
from .avaliacao_inline import AvaliacaoInline
from .comentario_inline import ComentarioInline


@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
        'modulo',
        'curso',
    ]

    search_fields = [
        'id',
        'titulo',
        'modulo__titulo',
    ]

    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'data_criacao',
        'data_alteracao',
    ]

    filter_horizontal = [
        'usuarios_concluintes',
    ]

    fieldsets = [
        ('Dados Principais', {'fields': (
			'titulo',
            'descricao',
			'video',
            'thumbnail',
            'modulo',
            'ordem',
            'usuarios_concluintes',
		)}),
        ('Dados de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    ]
    
    inlines = [
        AnexoVideoInline,
        AvaliacaoInline,
        ComentarioInline,
    ]
