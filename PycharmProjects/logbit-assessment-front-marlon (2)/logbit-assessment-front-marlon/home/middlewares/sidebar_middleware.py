#Shift + Alt + O para organizar as importações (vs code)

from curso.models import Curso
from django.http import HttpResponseForbidden
from home.views import home


class SidebarMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        return self.get_response(request)
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        id_args = view_kwargs.get('id_curso', None)
        id_request = request.GET.get('curso', None)

        id_curso = id_args or id_request
        curso = Curso.objects.filter(id=id_curso).first() if id_curso else None

        if curso and not \
        request.user in curso.usuarios_com_acesso.all():
            return HttpResponseForbidden()
        
        request.content_params.update({
            'curso': curso
        })
