from rest_framework.serializers import ModelSerializer
from core.models import Empresa

class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'id',
            'nome',
            'cnpj',
            'descricao',
            'cor_principal',
            'cor_secundaria',
            'logo',
            'data_alteracao',
            'data_criacao',
            'usuario_criacao',
            'usuario_atualizacao',
            ]