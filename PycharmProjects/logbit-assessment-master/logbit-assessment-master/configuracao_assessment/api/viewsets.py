from rest_framework .viewsets import ModelViewSet

from configuracao_assessment.models import (
                    ConfiguracaoAssessment,
                    ConfiguracaoPerguntaCheck,
                    ConfiguracaoPerguntaDiscursiva,
                    ConfiguracaoPerguntaObjetiva,
                    ConfiguracaoAlternativa,
                    ConfiguracaoAnexo
                    )
from . import (
            ConfiguracaoAssessmentSerializer,
            ConfiguracaoPerguntaCheckSerializer,
            ConfiguracaoPerguntaDiscursivaSerializer,
            ConfiguracaoPerguntaObjetivaSerializer,
            ConfiguracaoAlternativaSerializer,
            ConfiguracaoAnexoSerializer
            )

class ConfiguracaoAssessmentViewSet(ModelViewSet):
    queryset = ConfiguracaoAssessment.objects.all()
    serializer_class = ConfiguracaoAssessmentSerializer
    filterset_fields = [
        'id',
        'nome',
        'descricao',
        'empresa',
        'grupos',
        'usuarios',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]

class ConfiguracaoPerguntaCheckViewSet(ModelViewSet):
    queryset = ConfiguracaoPerguntaCheck.objects.all()
    serializer_class = ConfiguracaoPerguntaCheckSerializer
    filterset_fields = [
        'id',
        'titulo',
        'descricao',
        'resposta_esperada',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]

class ConfiguracaoPerguntaDiscursivaViewSet(ModelViewSet):
    queryset = ConfiguracaoPerguntaDiscursiva.objects.all()
    serializer_class = ConfiguracaoPerguntaDiscursivaSerializer
    filterset_fields = [
        'id',
        'titulo',
        'descricao',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]

class ConfiguracaoPerguntaObjetivaViewSet(ModelViewSet):
    queryset = ConfiguracaoPerguntaObjetiva.objects.all()
    serializer_class = ConfiguracaoPerguntaObjetivaSerializer
    filterset_fields = [
        'id',
        'titulo',
        'descricao',
        'alternativa_correta',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]

class ConfiguracaoAlternativaViewSet(ModelViewSet):
    queryset = ConfiguracaoAlternativa.objects.all()
    serializer_class = ConfiguracaoAlternativaSerializer
    filterset_fields = [
        'id',
        'titulo',
        'descricao',
        'configuracao_pergunta_objetiva',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]

class ConfiguracaoAnexoViewSet(ModelViewSet):
    queryset = ConfiguracaoAnexo.objects.all()
    serializer_class = ConfiguracaoAnexoSerializer
    filterset_fields = [
        'id',
        'titulo',
        'descricao',
        'data_alteracao',
        'data_criacao',
        'usuario_criacao',
        'usuario_atualizacao',
        ]