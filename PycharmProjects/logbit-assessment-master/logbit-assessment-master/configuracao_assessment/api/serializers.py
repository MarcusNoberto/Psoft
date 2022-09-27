from rest_framework.serializers import ModelSerializer
from configuracao_assessment.models import (
                    ConfiguracaoAssessment,
                    ConfiguracaoPerguntaCheck,
                    ConfiguracaoPerguntaDiscursiva,
                    ConfiguracaoPerguntaObjetiva,
                    ConfiguracaoAlternativa,
                    ConfiguracaoAnexo
                    )

class ConfiguracaoAssessmentSerializer(ModelSerializer):
    class Meta:
        model = ConfiguracaoAssessment
        fields = [
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

class ConfiguracaoPerguntaCheckSerializer(ModelSerializer):
    class Meta:
        model = ConfiguracaoPerguntaCheck
        fields = [
            'id',
            'titulo',
            'descricao',
            'resposta_esperada',
            'data_alteracao',
            'data_criacao',
            'usuario_criacao',
            'usuario_atualizacao',
            ]

class ConfiguracaoPerguntaDiscursivaSerializer(ModelSerializer):
    class Meta:
        model = ConfiguracaoPerguntaDiscursiva
        fields = [
            'id',
            'titulo',
            'descricao',
            'data_alteracao',
            'data_criacao',
            'usuario_criacao',
            'usuario_atualizacao',
            ]

class ConfiguracaoPerguntaObjetivaSerializer(ModelSerializer):
    class Meta:
        model = ConfiguracaoPerguntaObjetiva
        fields = [
            'id',
            'titulo',
            'descricao',
            'alternativa_correta',
            'data_alteracao',
            'data_criacao',
            'usuario_criacao',
            'usuario_atualizacao',
            ]

class ConfiguracaoAlternativaSerializer(ModelSerializer):
    class Meta:
        model = ConfiguracaoAlternativa
        fields = [
            'id',
            'titulo',
            'descricao',
            'configuracao_pergunta_objetiva',
            'data_alteracao',
            'data_criacao',
            'usuario_criacao',
            'usuario_atualizacao',
            ]

class ConfiguracaoAnexoSerializer(ModelSerializer):
    class Meta:
        model = ConfiguracaoAnexo
        fields = [
            'id',
            'titulo',
            'descricao',
            'data_alteracao',
            'data_criacao',
            'usuario_criacao',
            'usuario_atualizacao',
            ]