from rest_framework.viewsets import ModelViewSet

from curso.models import (
    AnexoVideo,
    Avaliacao,
    Comentario,
    Curso,
    Modulo,
    Video
)

from .serializers import (
    AnexoVideoSerializer,
    AvaliacaoSerializer,
    ComentarioSerializer,
    CursoSerializer,
    ModuloSerializer,
    VideoSerializer
)

from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

### Classe de paginação ###
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class AnexoVideoViewSets(ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = AnexoVideo.objects.all()
    serializer_class=AnexoVideoSerializer
    filterset_fields = ['video',]
    
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id']
    search_fields = [
        'usuario_criacao', 
        'usuario_alteracao', 
        'data_criacao', 
        'data_alteracao'
    ]

class AvaliacaoViewSets(ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Avaliacao.objects.all()
    serializer_class=AvaliacaoSerializer
    filterset_fields = ['nota', 'video']
    
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id']
    search_fields = [
        'usuario_criacao',
        'usuario_alteracao',
        'data_criacao',
        'data_alteracao',
    ]

class ComentarioViewSets(ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Comentario.objects.all()
    serializer_class=ComentarioSerializer
    filterset_fields = ['video',]
    
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id']
    search_fields = [
        'usuario_criacao', 
        'usuario_alteracao', 
        'data_criacao', 
        'data_alteracao'
    ]

class CursoViewSets(ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Curso.objects.all()
    serializer_class=CursoSerializer
    filterset_fields = ['titulo', 'usuarios_com_acesso']
    
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id']
    search_fields = [
        'usuario_criacao', 
        'usuario_alteracao', 
        'data_criacao', 
        'data_alteracao'
    ]

class ModuloViewSets(ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Modulo.objects.all()
    serializer_class=ModuloSerializer
    filterset_fields = ['curso']
    
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['ordem', 'id']
    search_fields = [
        'usuario_criacao', 
        'usuario_alteracao', 
        'data_criacao', 
        'data_alteracao'
    ]

class VideoViewSets(ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Video.objects.all()
    serializer_class=VideoSerializer
    filterset_fields = [
        'titulo',
        'modulo',
        'descricao'
    ]
    
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['ordem', 'id']
    search_fields = [
        'titulo',
        'descricao'
    ]