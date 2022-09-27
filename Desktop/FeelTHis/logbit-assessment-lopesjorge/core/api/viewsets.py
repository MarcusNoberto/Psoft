from rest_framework .viewsets import ModelViewSet

from core.models import Empresa
from . import EmpresaSerializer

class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    filterset_fields = [
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