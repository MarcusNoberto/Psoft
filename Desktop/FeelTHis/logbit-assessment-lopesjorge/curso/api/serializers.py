from rest_framework.serializers import ModelSerializer
from curso.models import (
    AnexoVideo,
    Avaliacao,
    Comentario,
    Curso,
    Modulo,
    Video

)

class AnexoVideoSerializer(ModelSerializer):
    class Meta:
        model = AnexoVideo
        fields = ('id','titulo','anexo','video','data_alteracao',
        'data_criacao','usuario_atualizacao','arquivo_icon')

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class ModuloSerializer(ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'titulo',
            'descricao',
            'video',
            'ordem',
            'data_criacao',
            'thumbnail',
            'usuarios_concluintes',
            'id_cap',
            'nome_capitulo',
            'nome_modulo',
            'id_modulo'
        ]