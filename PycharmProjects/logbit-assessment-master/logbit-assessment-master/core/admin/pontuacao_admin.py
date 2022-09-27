from django.contrib import admin

from ..models.pontuacao import Pontuacao


@admin.register(Pontuacao)
class PontuacaoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'pontuacao_bronze',
        'pontuacao_prata',
        'pontuacao_ouro'
    ]

    search_fields = [
        'id',
    ]
