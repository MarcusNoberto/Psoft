from core.models.empresa import Empresa
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


@admin.register(Empresa)
class EmpresaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'cnpj',
    ]

    search_fields = [
        'id',
        'nome',
        'cnpj',
    ]

    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'data_criacao',
        'data_alteracao',
    ]

    fieldsets = [
        ('Dados Principais', {'fields': (
			'nome',
			'cnpj',
            'descricao',
		)}),
        ('Configuração Principal', {'fields':(
            'cor_principal',
            'cor_secundaria',
            'logo',
        )}),
        ('Configuração de criação', {'fields': (
			'usuario_criacao',
			'usuario_atualizacao',
            'data_criacao',
            'data_alteracao',
		)}),
    ]
