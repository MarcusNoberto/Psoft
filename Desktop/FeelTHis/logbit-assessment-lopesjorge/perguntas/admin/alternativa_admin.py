from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from perguntas.models import Alternativa


@admin.register(Alternativa)
class AlternativaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
        'pergunta_multipla_escolha',
    ]
    
    search_fields = [
        'id',
        'titulo',
        'pergunta_multipla_escolha',
    ]
    
    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'data_criacao',
        'data_alteracao',
    ]
