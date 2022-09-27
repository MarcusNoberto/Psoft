from django.contrib import admin

from ..models import RegistroCapitulo


@admin.register(RegistroCapitulo)
class RegistroCapituloAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'usuario',
        'data_hora',
        'progresso',
        'modulo',
        'tipo'
    ]

    search_fields = [
        'id',
        'usuario',
        'data_hora',
        'progresso',
        'modulo',
        'tipo'
    ]

    readonly_fields=[
        'usuario',
        'progresso',
        'modulo',
        'tipo'
    ]

    
