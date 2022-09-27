#Shift + Alt + O para organizar as importações (vs code)

from functools import partial

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from funcoes_utilitarias.redirect import reverse_lazy_plus
from django.shortcuts import get_object_or_404, render
from respostas.models import Resposta

from ..models import PerguntaMultiplaEscolha, PerguntaObjetiva


@login_required
def responder_pergunta(request, tipo_pergunta, pergunta_id):
    if tipo_pergunta == 'pergunta_multipla_escolha':
        pergunta = get_object_or_404(PerguntaMultiplaEscolha, pk=pergunta_id)
        resposta = Resposta.objects.filter(
            usuario=request.user,
            pergunta_multipla_escolha=pergunta
        ).first()

        if not resposta:
            """ if pergunta.contem_mais_de_uma_resposta:
                lista_criacao_resposta=[]
                for resp in request.POST:
                    if "resposta" in resp:
                        criar_resposta = partial(Resposta.objects.create, pergunta_multipla_escolha=pergunta)
                        lista_criacao_resposta.append(criar_resposta)

            else: """
            criar_resposta = partial(Resposta.objects.create, pergunta_multipla_escolha=pergunta)
                
    elif tipo_pergunta == 'pergunta_objetiva':
        pergunta = get_object_or_404(PerguntaObjetiva, pk=pergunta_id)
        resposta = Resposta.objects.filter(
            usuario=request.user,
            pergunta_objetiva=pergunta
        ).first()

        if not resposta:
            criar_resposta = partial(Resposta.objects.create, pergunta_objetiva=pergunta)
    else:
        return HttpResponseNotFound('Tipo de pergunta inválida')
    
    context = {
        'pergunta': pergunta,
        'resposta': resposta,
        
        'title': pergunta.titulo,
    }
    
    if request.method == 'POST':
        if resposta:
            resposta.resposta = request.POST.get('resposta', None)
            resposta.save()
        else:
            criar_resposta(resposta=request.POST.get('resposta', None))
    
        return reverse_lazy_plus(
            'responder_pergunta',
            url_params=[
                tipo_pergunta,
                pergunta_id
            ],
            get_params={
                'curso': pergunta.modulo.curso.id
            }
        )

    
    return render(
        request,
        'perguntas/responder_pergunta.html',
        context
    )
