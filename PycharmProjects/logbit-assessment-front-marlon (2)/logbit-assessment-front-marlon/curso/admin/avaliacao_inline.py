from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Avaliacao


class AvaliacaoInline(admin.StackedInline):
    model = Avaliacao

    extra = 0

    classes = [
      'collapse',
    ]

    fieldsets = [
        ('Dados Principais', {'fields': (
			'nota',
            'feedback',
            'video',
		)}),
    ]
