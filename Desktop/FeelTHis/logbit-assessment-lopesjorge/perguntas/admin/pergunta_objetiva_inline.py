import nested_admin

from ..models import PerguntaObjetiva
from .alternativa_objetiva_inline import AlternativaObjetivaInline


class PerguntaObjetivaInline(nested_admin.NestedStackedInline):
    model = PerguntaObjetiva
    
    extra = 0

    autocomplete_fields = [
        'alternativa_correta',
    ]
    
    fields = [
        'titulo',
        'descricao',
        'alternativa_correta',
        'ordem',
    ]

    classes = [
        'collapse',
    ]

    inlines = [
        AlternativaObjetivaInline,
    ]
