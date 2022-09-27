#Shift + Alt + O para organizar as importações (vs code)
from curso.models import Curso
from avatar.models import Avatar 
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from curso.models import Modulo
from core.models import Profile
from curso.models import Video
from decouple import config
from curso.models import RegistroCapitulo
PRODUCAO = config('PRODUCAO', default=True, cast=bool)
from dateutil.relativedelta import relativedelta
from core.models import Fabricante
from datetime import datetime
from django.contrib.auth.decorators import login_required
from core.models.pontuacao import Pontuacao


@login_required
def home(request):
    
    if PRODUCAO:
        nome_fabricante = request.session['dados_usuario']['fabricanteName']
        fabricante = Fabricante.objects.get(nome_auth=nome_fabricante)
    else:
        fabricante = Fabricante.objects.get(nome_auth="TESTE")
    cursos = Curso.objects.filter(
        usuarios_com_acesso=request.user,
        linguagem=fabricante.linguagem
    ).order_by('id')

    
    
    mensagem = bool(request.GET.get('mensagem', None))
    id_curso_concluido = request.GET.get('curso', None)
    
    if id_curso_concluido:
        curso_concluido = get_object_or_404(Curso, id=id_curso_concluido)
    else:
        curso_concluido = None
    lista = []
    user = request.user

    pontuacao = Pontuacao.objects.all().first()
    bronze = pontuacao.pontuacao_bronze
    prata = pontuacao.pontuacao_prata
    ouro = pontuacao.pontuacao_ouro
    

    #Query dos dados
    lista_videos_progresso = []
    lista_quizz_progresso = []
    
    lista_progresso_videosaulas=RegistroCapitulo.objects.filter(
        modulo__in=cursos,
        usuario=request.user, 
        tipo='Progresso nas Videoaulas'
    ).order_by('data_hora')
    
    lista_progresso_perguntas = RegistroCapitulo.objects.filter(
        modulo__in = cursos,
        usuario=request.user, 
        tipo='Progresso no Quizz'
    ).order_by('data_hora')
    
        
    #Variaveis auxiliares
    data_time_atual = datetime.today()
    data_first_videoaulas = lista_progresso_videosaulas.first().data_hora if lista_progresso_videosaulas else data_time_atual
    data_last_videoaulas = lista_progresso_videosaulas.last().data_hora if lista_progresso_videosaulas else data_time_atual
    data_first_quizz = lista_progresso_perguntas.first().data_hora if lista_progresso_perguntas else data_time_atual
    data_last_quizz = lista_progresso_perguntas.last().data_hora if lista_progresso_perguntas else data_time_atual

    #Listagem das datas do Vídeo
    array_date_video = []
    while data_first_videoaulas <=data_last_videoaulas:
        array_date_video.append(data_first_videoaulas)
        data_first_videoaulas += relativedelta(months=1) 

    #Listagem das datas do Quizz
    array_date_quizz = []
    while data_first_quizz <=data_last_quizz:
        array_date_quizz.append(data_first_quizz)
        data_first_quizz += relativedelta(months=1) 


    #Listagem geral
    quantidade_cursos = len(cursos)

    listagem_geral_quizz =[]
    cache_ultimo_progresso = 0
    for data_base_quizz in array_date_quizz:
        

        progresso = 0
        if data_base_quizz.month == data_time_atual.month and data_base_quizz.year == data_time_atual.year:
            for curso in cursos:
                progresso+=curso.progresso_quizz
            progresso = progresso/(quantidade_cursos or 1)
        else:
            registros_atuais = lista_progresso_perguntas.filter(data_hora__month=data_base_quizz.month, data_hora__year=data_base_quizz.year)
            registros = []
            for curso in cursos:
                registros.append(
                    registros_atuais.filter(
                        modulo=curso
                    ).last()
                )
            for rg in registros:
                progresso+=(rg.progresso if rg else 0)
            progresso = progresso/(quantidade_cursos or 1)
            progresso = progresso if progresso > 0 else cache_ultimo_progresso

        if progresso > 0:
            cache_ultimo_progresso = progresso

        listagem_geral_quizz.append(
            {
                "data": data_base_quizz,
                "progresso": round(float(progresso), 2)
            }
        )

    listagem_geral_video =[]
    cache_ultimo_progresso = 0
    for data_base_video in array_date_video:
        

        progresso = 0
        if data_base_video.month == data_time_atual.month and data_base_video.year == data_time_atual.year:
            for curso in cursos:
                progresso+=curso.progresso_video
            progresso = progresso/(quantidade_cursos or 1)
        else:
            registros_atuais = lista_progresso_perguntas.filter(data_hora__month=data_base_video.month, data_hora__year=data_base_video.year)
            registros = []
            for curso in cursos:
                registros.append(
                    registros_atuais.filter(
                        modulo=curso
                    ).last()
                )
            for rg in registros:
                progresso+=(rg.progresso if rg else 0)
            progresso = progresso/(quantidade_cursos or 1)
            progresso = progresso if progresso > 0 else cache_ultimo_progresso

        if progresso > 0:
            cache_ultimo_progresso = progresso

        listagem_geral_video.append(
            {
                "data": data_base_video,
                "progresso": round(float(progresso), 2)
            }
        )
    
    #Listagem por curso
    for curso in cursos:
        lista_progresso_videosaulas = RegistroCapitulo.objects.filter(
            modulo = curso,
            usuario=request.user, 
            tipo='Progresso nas Videoaulas'
        ).order_by('data_hora')
        
        lista_progresso_perguntas = RegistroCapitulo.objects.filter(
            modulo = curso,
            usuario=request.user, 
            tipo='Progresso no Quizz'
        ).order_by('data_hora')

        listagem_quizz_registros =[]
        cache_ultimo_progresso = 0
        for data_base_quizz in array_date_quizz:
            

            if data_base_quizz.month == data_time_atual.month and data_base_quizz.year == data_time_atual.year:
                progresso = curso.progresso_quizz
            else:
                registro_atual = lista_progresso_perguntas.filter(data_hora__month=data_base_quizz.month, data_hora__year=data_base_quizz.year).last()
                progresso = registro_atual.progresso if registro_atual else cache_ultimo_progresso

            if progresso > 0:
                cache_ultimo_progresso = progresso

            listagem_quizz_registros.append(
                {
                    "data": data_base_quizz,
                    "progresso": round(float(progresso), 2)
                }
            )

        listagem_videos_registros =[]
        cache_ultimo_progresso = 0
        for data_base_video in array_date_video:
            
        
            if data_base_video.month == data_time_atual.month and data_base_video.year == data_time_atual.year:
                progresso = curso.progresso_video
            else:
                registro_atual = lista_progresso_videosaulas.filter(data_hora__month=data_base_video.month, data_hora__year=data_base_video.year).last()
                progresso = registro_atual.progresso if registro_atual else cache_ultimo_progresso

            if progresso > 0:
                cache_ultimo_progresso = progresso

            listagem_videos_registros.append(
                {
                    "data": data_base_video,
                    "progresso": round(float(progresso), 2)
                }
            )


        lista_videos_progresso.append(
            {
                'curso': curso,
                'lista_registros': listagem_videos_registros
            }
        )
        lista_quizz_progresso.append(
            {
                'curso': curso,
                'lista_registros': listagem_quizz_registros
            }
        )
    
    ###
    profile = Profile.objects.filter(user = user).first()
    if profile:
        acesso_julho = profile.acessos_mes(7)
        acesso_agosto = profile.acessos_mes(8)
        acesso_setembro = profile.acessos_mes(9)
        acesso_outubro = profile.acessos_mes(10)
        acesso_novembro = profile.acessos_mes(11)
        acesso_dezembro = profile.acessos_mes(12)
    else:
        acesso_julho = 0
        acesso_agosto = 0
        acesso_setembro = 0
        acesso_outubro = 0
        acesso_novembro = 0
        acesso_dezembro = 0
    porcentagem_modulos = []
    videos_concluidos_modulo = 0
    total_videos_modulo = 0
    if PRODUCAO:
        nome_fabricante = request.session['dados_usuario']['fabricanteName']
        fabricante = Fabricante.objects.get(nome_auth=nome_fabricante)
    else:
        fabricante = Fabricante.objects.get(nome_auth="TESTE")

    modulos = Modulo.objects.filter(curso__linguagem=fabricante.linguagem).distinct()
    cr = Curso.objects.all()
    cursos = Curso.objects.filter(linguagem=fabricante.linguagem)
    total_modulos = cursos.count()
    aux = 0
    modulo_mais_proximo = 0
    modulos_concluidos = []
    perguntas_concluidas = []
    pergunta_modulo = None
    porcentagem = 0
    perguntas_falta = 1000
    perguntas = 0
    perguntas_acerto = 0
    list_modulo = []
    primeira_pergunta = []
    
    for modulo in modulos:
        videos_concluidos_modulo += modulo.videos_desse_modulo().quantidade_videos_concluidos
        total_videos_modulo += modulo.videos_desse_modulo().total_videos
        primeira_pergunta.append(modulo.primeira_pergunta)
        lista.append(modulo.primeiro_video_do_modulo)
        porcentagem_modulos.append(modulo.progresso_modulo().progresso_total)
        perguntas += modulo.perguntas_desse_modulo().total_perguntas
        perguntas_acerto += modulo.perguntas_desse_modulo().quantidade_perguntas_respondidas
        curso = Curso.objects.filter(modulo = modulo).first()
        if curso.get_progresso_perguntas == 100:
            perguntas_concluidas.append(curso)
        if perguntas_acerto < perguntas:
            if (perguntas - perguntas_acerto) < perguntas_falta:
                perguntas_falta = perguntas - perguntas_acerto
                porcentagem = (perguntas_acerto/perguntas or 1)*100
                curso = Curso.objects.filter(modulo = modulo).first()
                pergunta_modulo = curso
    
    try:
        primeiro_video = cursos.first().modulo_set.first().video_set.first()
    except:
        primeiro_video = None
    
    
    for curso in cursos:
        if curso.curso_concluido:
            modulos_concluidos.append(curso.titulo)
        else:
            progresso = float(curso.progresso_curso().progresso_total)
            if progresso > aux:
                modulo_mais_proximo = curso
                aux = abs(float(curso.get_porcentagem_progresso))
    for curso in cr:
        list_modulo.append(curso.get_porcentagem_progresso)

    cursos_com_acesso = Curso.objects.filter(linguagem=fabricante.linguagem) 

    next_aulas = []
    ultimo_registro_com_video = RegistroCapitulo.objects.filter(
        video__isnull=False,
        usuario=request.user, 
        tipo='Progresso nas Videoaulas'
    ).order_by('data_hora').last()
    video_direcionado = None
    videos = Video.objects.all()

    usuario_completo = True
    for video in videos:
        if video.modulo.curso == modulo_mais_proximo:
            if not request.user in video.usuarios_concluintes.all():
                next_aulas.append(video)
                video_direcionado = video
        if request.user not in video.usuarios_concluintes.all():
                usuario_completo= False
    usuario_novo = False
    a = False
    usuario_normal = False
    if RegistroCapitulo.objects.filter(usuario=request.user).exists():
        usuario_normal = True
    else:
        usuario_novo = True

    
    
 
    context = {
        'cursos': cursos,
        'modulos':modulos,
        'mensagem': mensagem,
        'lista':lista,
        'profile': profile,
        'videos_concluidos' : videos_concluidos_modulo,
        'total_modulos': total_modulos,
        'total_videos': total_videos_modulo,
        'curso_concluido': curso_concluido,
        'ultima_aula_usuario': lista_progresso_videosaulas.last().data_hora if lista_progresso_videosaulas.last() else None,
        'data_ultima_aula': profile.data_ultima_aula if profile else None,
        'acesso_julho': acesso_julho,
        'acesso_agosto':acesso_agosto,
        'acesso_setembro': acesso_setembro,
        'acesso_outubro': acesso_outubro,
        'acesso_novembro': acesso_novembro,
        'acesso_dezembro': acesso_dezembro,
        'modulos_concluidos': modulos_concluidos,
        'modulo_mais_proximo' : modulo_mais_proximo,
        'primeiro_acesso': profile.usuario_novo if profile else None,
        'progresso_mais_proximo' : 100 - aux,
        'total_perguntas' : perguntas,
        'perguntas_respondidas' : perguntas_acerto if perguntas_acerto else 0,
        'modulo_perguntas_concluidas' : perguntas_concluidas if perguntas_concluidas else None,
        'porcentagem' : porcentagem,
        'pergunta_modulo' : pergunta_modulo,
        'primeiro_acesso' : profile.usuario_novo if profile else False,
        'list_modulo' : list_modulo,
        'cursos_com_acesso':cursos_com_acesso,
        'ultimo_registro_com_video': ultimo_registro_com_video,
        'lista_videos_progresso': lista_videos_progresso,
        'lista_quizz_progresso':lista_quizz_progresso,
        'array_date_quizz': array_date_quizz,
        'array_date_video': array_date_video,
        'primeiro_video' : primeiro_video,
        'listagem_geral_video': listagem_geral_video,
        'listagem_geral_quizz': listagem_geral_quizz,
        'tamanho_listagem_geral_video': len(listagem_geral_video),
        'tamanho_listagem_geral_quizz': len(listagem_geral_quizz),
        'bronze' : bronze,
        'prata' : prata,
        'ouro' : ouro,
        'video_direcionado' : video_direcionado if video_direcionado else 1,
        'usuario_normal' : usuario_normal,
        'next_aulas' : next_aulas,
        'usuario_completo' : usuario_completo,
        'usuario_novo' : usuario_novo
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
