#Shift + Alt + O para organizar as importações (vs code)

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import DicaOportunidade


@admin.register(DicaOportunidade)
class DicaOportunidadeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'pergunta',
        'dica',
        'aula_sugerida',
    ]

    search_fields = [
        'id',
        'pergunta_multipla_escolha__titulo',
        'aula_sugerida__titulo',
    ]

    autocomplete_fields = [
        'pergunta_multipla_escolha',
        'aula_sugerida',
    ]

    exclude = [
        'pergunta_objetiva',
    ]
