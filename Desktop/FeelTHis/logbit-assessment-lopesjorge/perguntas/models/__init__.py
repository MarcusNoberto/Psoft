#Shift + Alt + O para organizar as importações (vs code)

from .alternativa import Alternativa
from .pergunta_multipla_escolha import PerguntaMultiplaEscolha
from .pergunta_objetiva import PerguntaObjetiva

__all__ = [
    Alternativa,
    PerguntaMultiplaEscolha,
    PerguntaObjetiva,
]
