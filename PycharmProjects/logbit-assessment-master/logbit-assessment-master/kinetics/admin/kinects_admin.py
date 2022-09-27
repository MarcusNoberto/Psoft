from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Kinetics


@admin.register(Kinetics)
class KineticsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'project_id',
        'project_url',
    ]

    search_fields = [
        'id',
        'name',
        'project_id',
        'project_url',
    ]

    fieldsets = [
        ('Dados principais', {'fields': [
            'name',
            'description',
            'project_id',
            'secret',
        ]}),
        ('URLs', {'fields': [
            'project_url',
            'url_base',
            'url_api',
            'url_redirect',
        ]})
    ]
