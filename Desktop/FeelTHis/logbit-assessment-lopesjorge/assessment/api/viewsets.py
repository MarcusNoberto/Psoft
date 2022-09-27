from assessment.models import (Anexo, Assessment, ItemAnexo, PerguntaCheck,
                               PerguntaDiscursiva, PerguntaObjetiva)
from perguntas.models import Alternativa
from rest_framework.viewsets import ModelViewSet

from . import (AlternativaSerializer, AnexoSerializer, AssessmentSerializer,
               ItemAnexoSerializer, PerguntaCheckSerializer,
               PerguntaDiscursivaSerializer, PerguntaObjetivaSerializer)


class AssessmentViewSet(ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    filterset_fields = [
        'id',
        'nome',
        'descricao',
        'usuario',
        'configuracao_assessment',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]

class AnexoAnoViewSet(ModelViewSet):
    queryset = Anexo.objects.all()
    serializer_class = AnexoSerializer
    filterset_fields = [
        'id',
        'titulo',
        'descricao',
        'assessment',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]

class ItemAnexoViewSet(ModelViewSet):
    queryset = ItemAnexo.objects.all()
    serializer_class = ItemAnexoSerializer
    filterset_fields = [
        'id',
        'arquivo',
        'anexo',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]

class PerguntaCheckViewSet(ModelViewSet):
    queryset = PerguntaCheck.objects.all()
    serializer_class = PerguntaCheckSerializer
    filterset_fields = [
        'id',
        'titulo',
        'descricao',
        'resposta_esperada',
        'resposta',
        'assessment',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]

class PerguntaDiscursivaViewSet(ModelViewSet):
    queryset = PerguntaDiscursiva.objects.all()
    serializer_class = PerguntaDiscursivaSerializer
    filterset_fields = [
        'id',
        'titulo',
        'descricao',
        'resposta',
        'assessment',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]

class PerguntaObjetivaViewSet(ModelViewSet):
    queryset = PerguntaObjetiva.objects.all()
    serializer_class = PerguntaObjetivaSerializer
    filterset_fields = [
        'id',
        'titulo',
        'descricao',
        'alternativa_correta',
        'resposta',
        'assessment',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]

class AlternativaViewSet(ModelViewSet):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer
    filterset_fields = [
        'id',
        'titulo',
        'descricao',
        'pergunta_objetiva',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]
