from assessment.models import (Anexo, Assessment, ItemAnexo, PerguntaCheck,
                               PerguntaDiscursiva, PerguntaObjetiva)
from django.db import models
from perguntas.models import Alternativa
from rest_framework.serializers import ModelSerializer


class AssessmentSerializer(ModelSerializer):
    class Meta:
        model = Assessment
        fields = [
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

class AnexoSerializer(ModelSerializer):
    class Meta:
        model = Anexo
        fields = [
            'id',
            'titulo',
            'descricao',
            'assessment',
            'data_alteracao',
            'data_criacao',
            'usuario_criacao',
            'usuario_atualizacao',
            ]

class ItemAnexoSerializer(ModelSerializer):
    class Meta:
        model = ItemAnexo
        fields = [
            'id',
            'arquivo',
            'anexo',
            'data_alteracao',
            'data_criacao',
            'usuario_criacao',
            'usuario_atualizacao',
            ]

class PerguntaCheckSerializer(ModelSerializer):
    class Meta:
        model = PerguntaCheck
        fields = [
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

class PerguntaDiscursivaSerializer(ModelSerializer):
    class Meta:
        model = PerguntaDiscursiva
        fields = [
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

class PerguntaObjetivaSerializer(ModelSerializer):
    class Meta:
        model = PerguntaObjetiva
        fields = [
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

class AlternativaSerializer(ModelSerializer):
    class Meta:
        model = Alternativa
        fields = [
            'id',
            'titulo',
            'descricao',
            'pergunta_objetiva',
            'data_alteracao',
            'data_criacao',
            'usuario_criacao',
            'usuario_atualizacao',
            ]
