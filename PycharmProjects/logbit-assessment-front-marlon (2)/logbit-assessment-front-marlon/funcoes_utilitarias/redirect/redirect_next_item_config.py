from functools import partial

from crum import get_current_user
from django.http import HttpResponseRedirect

from .reverse_lazy_plus import reverse_lazy_plus


def redirect_next_item_config(video_pergunta: object) -> HttpResponseRedirect:
    '''
    Params:
        video_pergunta = Video ou PerguntaMultiplaEscolha
    
    Função para retornar o redirecionamento para a próxima
    pergunta ou para o próximo vídeo.
    '''

    itens = get_all_itens(video_pergunta)
    next_itens = get_next_itens(video_pergunta, itens)

    if next_itens:
        next_item = next_itens[0]
        redirect = make_partial(next_item, video_pergunta)

        if next_item.url_redirect == 'responder_pergunta':
            return redirect_pergunta(redirect, next_item)
        
        elif next_item.url_redirect == 'video:video':
            return redirect_video(redirect, next_item)
    
    curso = video_pergunta.modulo.curso
    if curso.ultimo_item == video_pergunta:
        return reverse_lazy_plus(
            'home',
            get_params={
                'curso': curso.id
            }
        )
    else:
        return redirect_conclusao(video_pergunta, 'conclusao_modulo')

#ANCHOR funções auxiliares
def get_all_itens(video_pergunta):
    return video_pergunta.modulo.get_all_itens().all_itens

def get_next_itens(video_pergunta, itens):
    # Old
    # return list(
    #     filter(lambda item: item.ordem > video_pergunta.ordem, itens)
    # )
    
    return list(
        filter(
            lambda item: # Cada item da lista
            not tem_check(item) and item.ordem > video_pergunta.ordem, # Condições que eu quero
            itens # Lista
        )
    )

def tem_check(video_pergunta):
    user = get_current_user()

    if video_pergunta.tipo == 'video':
        return user in video_pergunta.usuarios_concluintes.all()
    elif video_pergunta.tipo == 'pergunta_multipla_escolha':
        return video_pergunta.resposta_set.all().exists()
    else:
        return False

def make_partial(next_item, video_pergunta):
    return partial(
        reverse_lazy_plus,
        url_name=next_item.url_redirect,
        get_params={
            'curso': next_item.modulo.curso.id
        },
        just_uri=True if video_pergunta.tipo == 'video' else False
    )

def redirect_pergunta(redirect_function, pergunta):
    return redirect_function(
        url_params=[
            pergunta.tipo,
            pergunta.id
        ]
    )

def redirect_video(redirect_function, video):
    return redirect_function(
        url_params=[
            video.modulo.id,
            video.id
        ]
    )

def redirect_conclusao(video_pergunta, url_name):
    return reverse_lazy_plus(
        url_name,
        url_params=[
            video_pergunta.modulo.id # id do módulo
        ],
        get_params={
            'curso': video_pergunta.modulo.curso.id # id do curso
        }
    )
