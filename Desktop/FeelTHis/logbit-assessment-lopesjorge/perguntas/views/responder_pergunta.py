#Shift + Alt + O para organizar as importações (vs code)

from functools import partial

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from funcoes_utilitarias.redirect import redirect_next_item_config
from perguntas.models import Alternativa
from respostas.models import Resposta

from ..models import PerguntaMultiplaEscolha, PerguntaObjetiva
from curso.models import RegistroCapitulo
from datetime import datetime
@login_required
def responder_pergunta(request, tipo_pergunta, pergunta_id, slug_projeto):
    if tipo_pergunta == 'pergunta_multipla_escolha':
        pergunta = get_object_or_404(PerguntaMultiplaEscolha, pk=pergunta_id)
        
        respostas = pergunta.resposta_set.filter(usuario=request.user)
        
        criar_resposta = partial(Resposta.objects.create, pergunta_multipla_escolha=pergunta)

    elif tipo_pergunta == 'pergunta_objetiva':
        pergunta = get_object_or_404(PerguntaObjetiva, pk=pergunta_id)
        respostas = pergunta.resposta_set.filter(usuario=request.user)

        criar_resposta = partial(Resposta.objects.create, pergunta_objetiva=pergunta)
    else:
        return HttpResponseNotFound('Tipo de pergunta inválida')
    
    if pergunta.modulo.class_sidebar == 'disabled':
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        if pergunta.contem_mais_de_uma_resposta:
            pergunta.resposta_set.all().delete()
            for resp in request.POST:
                if "resposta" in resp:
                    id_alternativa = request.POST[resp]
                    alternativa = Alternativa.objects.filter(id=id_alternativa).first()

                    criar_resposta(
                        resposta=alternativa.titulo
                    )

        else:
            if respostas:
                resposta = respostas.first()
                resposta.resposta = request.POST.get('resposta', None)
                resposta.save()
            else:
                criar_resposta(resposta=request.POST.get('resposta', None))
        modulo = pergunta.modulo.curso
        RegistroCapitulo.objects.create(
            modulo=modulo,
            usuario=request.user,
            data_hora=datetime.today(),
            progresso=modulo.progresso_quizz,
            tipo='Progresso no Quizz'
        )
        
        return redirect_next_item_config(pergunta)

    modulo = pergunta.modulo
    todas_perguntas_do_modulo = modulo.get_perguntas()
    
    context = {
        'perguntas': todas_perguntas_do_modulo,
        'pergunta': pergunta,
        'respostas_titles': [resposta.resposta for resposta in respostas],
        
        'title': pergunta.titulo,
    }
    
    return render(
        request,
        'perguntas/responder_pergunta.html',
        context
    )
