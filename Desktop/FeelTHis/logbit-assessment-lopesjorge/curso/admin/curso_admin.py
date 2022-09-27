from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Curso
from .modulo_inline import ModuloInline


@admin.register(Curso)
class CursoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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

    filter_horizontal = [
        'usuarios_com_acesso',
        'pre_requisito',
    ]
    
    fieldsets = [
        ('Dados Principais', {'fields': (
            'linguagem',
			'titulo',
            'icone',
            'projeto',
            'descricao',
            'foto_capa',
            'usuarios_com_acesso',
		)}),
        ('Pré-requisitos', {'fields': [
            'score_minimo',
            'progresso_minimo',
            'pre_requisito',
            'pontuacao_bronze',
            'pontuacao_prata',
            'pontuacao_ouro'
        ]}),
        ('Dados de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    ]

    inlines = [
        ModuloInline,
    ]
