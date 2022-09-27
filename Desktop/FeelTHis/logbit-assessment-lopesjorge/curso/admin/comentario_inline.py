from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Comentario


class ComentarioInline(admin.StackedInline):
    model = Comentario

    extra = 0

    classes = [
      'collapse',
    ]

    fieldsets = [
      ('Dados Principais', {'fields': (
        'comentario',
      )}),
    ]
