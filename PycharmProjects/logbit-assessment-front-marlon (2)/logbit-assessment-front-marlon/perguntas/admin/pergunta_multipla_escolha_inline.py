import nested_admin

from ..models import PerguntaMultiplaEscolha
from .alternativa_multipla_escolha_inline import AlternativaMultiplaEscolhaInline


class PerguntaMultiplaEscolhaInline(nested_admin.NestedStackedInline):
    model = PerguntaMultiplaEscolha

    extra = 0

    fields = [
        'titulo',
        'contem_mais_de_uma_resposta',
        'descricao',
        'valor_minimo',
        'modulo',
        'ordem',
        'nota_maxima',
        'pontos_conquistados',
        'score_pergunta'
    ]

    readonly_fields=['nota_maxima', 'pontos_conquistados', 'score_pergunta']

    classes = [
        'collapse',
    ]

    inlines = [
        AlternativaMultiplaEscolhaInline,
    ]
