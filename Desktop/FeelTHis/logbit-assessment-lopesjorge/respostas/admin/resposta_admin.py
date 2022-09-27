#Shift + Alt + O para organizar as importações (vs code)

from operator import truediv
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Resposta


@admin.register(Resposta)
class RespostaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'resposta',
        'usuario',
        'curso',
        'pergunta',
        'pontuacao',
        'data_criacao',
    ]

    list_filter = [
        'usuario',
        'pontuacao',
        'data_criacao',
    ]

    readonly_fields = [
        'pergunta',
        'correta',
        'pontuacao',
    ]

    search_fields = [
        'resposta',
        'usuario__username',
        'pergunta__titulo',
        'pontuacao',
        'data_criacao',
    ]

    fields = [
        'resposta',
        'usuario',
        'pergunta',
        'pontuacao',
        'correta',
    ]
    
    def get_fields(self, request, obj=None):
        fields = self.fields
        if obj:
            if obj.pontuacao:
                fields.remove('correta') if 'correta' in fields else None
                fields.append('pontuacao') if 'pontuacao' not in fields else None
            else:
                fields.remove('pontuacao') if 'pontuacao' in fields else None
                fields.append('correta') if 'correta' not in fields else None
        else:
            fields.remove('pontuacao') if 'pontuacao' in fields else None
            fields.remove('correta') if 'correta' in fields else None
        
        return fields

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
