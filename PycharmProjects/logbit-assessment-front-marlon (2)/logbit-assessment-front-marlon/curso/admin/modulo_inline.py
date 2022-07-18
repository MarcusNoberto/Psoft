from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Modulo


class ModuloInline(admin.StackedInline):
    model = Modulo

    extra = 0

    fieldsets = [
        ('Dados Principais', {'fields': (
			'titulo',
            'descricao',
            'ordem',
		)}),
    ]
