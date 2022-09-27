import nested_admin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from perguntas.models import Alternativa


class AlternativaMultiplaEscolhaInline(nested_admin.NestedTabularInline):
    model = Alternativa

    extra = 0

    fields = [
        'titulo',
        'descricao',
        'valor',
    ]

    classes = [
        'collapse',
    ]
