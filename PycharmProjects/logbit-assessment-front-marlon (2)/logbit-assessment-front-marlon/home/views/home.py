#Shift + Alt + O para organizar as importações (vs code)
from curso.models import Curso
from avatar.models import Avatar 
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy




def home(request):
    if request.user.is_authenticated:
        cursos = Curso.objects.filter(
            usuarios_com_acesso=request.user
        ).order_by('id')
    else:
        cursos = None
    
    mensagem = bool(request.GET.get('mensagem', None))
    id_curso_concluido = request.GET.get('curso', None)
    
    if id_curso_concluido:
        curso_concluido = get_object_or_404(Curso, id=id_curso_concluido)
    else:
        curso_concluido = None

    context = {
        'cursos': cursos,
        'mensagem': mensagem,

        'curso_concluido': curso_concluido,
    }

    return render(
        request,
        'homepage/home.html',
        context
    )


def url_alterar_foto(request):
    avatar = Avatar.objects.filter(user=request.user).last()
    avatar = Avatar(user=request.user, primary=True) if not avatar else avatar
    foto = request.FILES.get('avatar', None)
    url = request.POST['url']
    if foto:
        avatar.avatar.save(foto.name, foto)
        avatar.save()

    return redirect(url)
