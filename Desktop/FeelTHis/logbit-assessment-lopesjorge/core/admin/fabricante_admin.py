from django.contrib import admin

from ..models import Fabricante
from import_export.admin import ImportExportModelAdmin


@admin.register(Fabricante)
class FabricanteAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'nome_fabricante',
        'nome_auth',
        'linguagem'
    ]

    search_fields = [
        'id',
        'nome',
        'linguagem'
    ]
