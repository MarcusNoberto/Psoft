from perguntas.models import PerguntaObjetiva

from assessment.models.anexo import Anexo
from assessment.models.assessment import Assessment
from assessment.models.item_anexo import ItemAnexo
from assessment.models.pergunta_check import PerguntaCheck
from assessment.models.pergunta_discursiva import PerguntaDiscursiva

__all__ = [
    Assessment,
    Anexo,
    ItemAnexo,
    PerguntaCheck,
    PerguntaDiscursiva,
    PerguntaObjetiva,
]
