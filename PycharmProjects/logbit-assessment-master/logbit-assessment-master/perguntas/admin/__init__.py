#Shift + Alt + O para organizar as importações (vs code)

from .alternativa_admin import AlternativaAdmin
from .alternativa_multipla_escolha_inline import \
    AlternativaMultiplaEscolhaInline
# from .alternativa_objetiva_inline import AlternativaObjetivaInline
from .pergunta_multipla_escolha_admin import PerguntaMultiplaEscolhaAdmin
from .pergunta_multipla_escolha_inline import PerguntaMultiplaEscolhaInline
# from .pergunta_objetiva_admin import PerguntaObjetivaAdmin
# from .pergunta_objetiva_inline import PerguntaObjetivaInline

__all__ = [
    AlternativaAdmin,
    AlternativaMultiplaEscolhaInline,
    # AlternativaObjetivaInline,

    PerguntaMultiplaEscolhaAdmin,
    PerguntaMultiplaEscolhaInline,

    # PerguntaObjetivaAdmin,
    # PerguntaObjetivaInline,
]
