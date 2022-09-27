from django.contrib import admin

from ..models import Instrucao


@admin.register(Instrucao)
class InstrucaoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'linguagem'
    ]

    search_fields = [
        'id',
    ]

