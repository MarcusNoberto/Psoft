from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import AnexoVideo


class AnexoVideoInline(admin.StackedInline):
    model = AnexoVideo

    extra = 0

    classes = [
      'collapse',
    ]

    fieldsets = [
        ('Dados Principais', {'fields': (
            'titulo',
			'anexo',
		)}),
    ]
