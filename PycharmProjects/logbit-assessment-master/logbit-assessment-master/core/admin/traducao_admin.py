from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from ..models import Traducao


@admin.register(Traducao)
class TraducaoAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'espanhol',
        'portugues',
        'ingles',
    ]

    search_fields = [
        'id',
        'espanhol',
        'portugues',
        'ingles',
    ]
