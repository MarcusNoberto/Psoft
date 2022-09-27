from django.contrib import admin

from ..models.projeto import Projeto


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
    ]

    search_fields = [
        'id',
        'titulo',
    ]

    readonly_fields = [
        'usuario_criacao',
        'usuario_atualizacao',
        'data_criacao',
        'data_alteracao',
    ]
