import nested_admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django_object_actions import DjangoObjectActions

from ..models import ConfiguracaoAssessment



# @admin.register(ConfiguracaoAssessment)
class ConfiguracaoAssessmentAdmin(DjangoObjectActions, ImportExportModelAdmin, nested_admin.NestedModelAdmin):
    list_display = [
        'id',
        'nome',
        'empresa',
    ]

    search_fields = [
        'id',
        'nome',
    ]

    filter_horizontal = [
        'grupos',
        'usuarios',
    ]

    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'data_criacao',
        'data_alteracao',
    ]

    fieldsets = (
        ('Dados Principais', {'fields': (
			'nome',
			'descricao',
			'empresa',
		)}),
        ('Configuração Pincipal', {'fields': (
			'grupos',
			'usuarios',
		)}),
        ('Configuração de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    )

    change_actions = [
        'gerar_configuracoes',
    ]

    

    def gerar_configuracoes(self, request, obj):
        obj.gerar_configuracoes()

    gerar_configuracoes.label = 'Gerar Configurações'
    gerar_configuracoes.short_description = 'Clique para gerar as configurações de acordo com a configuração informada'
