#Shift + Alt + O para organizar as importações (vs code)
from curso.models import Curso
from avatar.models import Avatar 
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from curso.models import Modulo
from core.models import Profile



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
    lista = []
    user = request.user

    profile = Profile.objects.filter(user = user)
    videos_concluidos_modulo = 0
    total_videos_modulo = 0
    modulos = Modulo.objects.all()
    for modulo in modulos:
        videos_concluidos_modulo += modulo.videos_desse_modulo.quantidade_videos_concluidos
        total_videos_modulo += modulo.videos_desse_modulo.total_videos
        lista.append(modulo.primeiro_video_do_modulo)

    context = {
        'cursos': cursos,
        'modulos':modulos,
        'mensagem': mensagem,
        'lista':lista,
        'profile': profile,
        'videos_concluidos' : videos_concluidos_modulo,
        'total_videos': total_videos_modulo,
        'curso_concluido': curso_concluido,
        'ultima_aula_usuario': profile.ultima_aula_vizualizada,
        'data_ultima_aula': profile.data_ultima_aula
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
