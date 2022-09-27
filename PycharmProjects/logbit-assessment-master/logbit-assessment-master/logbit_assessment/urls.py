'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from assessment.api.viewsets import (AlternativaViewSet, AnexoAnoViewSet,
                                     AssessmentViewSet,
                                     ItemAnexoViewSet, PerguntaCheckViewSet,
                                     PerguntaDiscursivaViewSet,
                                     PerguntaObjetivaViewSet)
from configuracao_assessment.api.viewsets import (
    ConfiguracaoAlternativaViewSet, ConfiguracaoAnexoViewSet,
    ConfiguracaoAssessmentViewSet,
    ConfiguracaoPerguntaCheckViewSet, ConfiguracaoPerguntaDiscursivaViewSet,
    ConfiguracaoPerguntaObjetivaViewSet)
from core.api.viewsets import EmpresaViewSet
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.urls import path
from curso.views.curso_views.projeto import projeto
from rest_framework import routers
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


router = routers.DefaultRouter()
router.register(r'assessment', AssessmentViewSet)
router.register(r'anexo_ano', AnexoAnoViewSet)
router.register(r'item_anexo', ItemAnexoViewSet)
router.register(r'pergunta_check', PerguntaCheckViewSet)
router.register(r'pergunta_discursiva', PerguntaDiscursivaViewSet)
router.register(r'pergunta_objetiva', PerguntaObjetivaViewSet)
router.register(r'alternativa', AlternativaViewSet)
router.register(r'configuracao_assessment', ConfiguracaoAssessmentViewSet)
router.register(r'configuracao_pergunta_check', ConfiguracaoPerguntaCheckViewSet)
router.register(r'configuracao_pergunta_discursiva', ConfiguracaoPerguntaDiscursivaViewSet)
router.register(r'configuracao_pergunta_objetiva', ConfiguracaoPerguntaObjetivaViewSet)
router.register(r'configuracao_alternativa', ConfiguracaoAlternativaViewSet)
router.register(r'configuracao_anexo', ConfiguracaoAnexoViewSet)
router.register(r'empresa', EmpresaViewSet)

### APP Curso
from curso.api.viewsets import (AnexoVideoViewSets, AvaliacaoViewSets,
                                ComentarioViewSets, CursoViewSets,
                                ModuloViewSets, VideoViewSets)

router.register(r'anexos_video', AnexoVideoViewSets)
router.register(r'avaliacoes', AvaliacaoViewSets) 
router.register(r'comentarios', ComentarioViewSets)
router.register(r'cursos', CursoViewSets)
router.register(r'modulos', ModuloViewSets)
router.register(r'videos', VideoViewSets)


urlpatterns = [
    path('', include('assessment.urls')),
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),

    path('', include('home.urls')),
    path('<slug:slug>/', projeto, name='projeto'),

    path('cursos/', include('curso.urls')),
    path('perguntas/', include('perguntas.urls')),

    path('kinetics/''', include('kinetics.urls')),

    path('api/', include(router.urls)),
    path('avatar/', include('avatar.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
