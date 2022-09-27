from assessment.models import (Assessment, PerguntaCheck, PerguntaDiscursiva,
                               PerguntaObjetiva)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy


@login_required
def avaliacao(request, id_avaliacao, tipo_pergunta, id_pergunta):
    usuario = request.user
    curso = User.objects.get(username=usuario).curso_set.first()
    modulos = curso.modulo_set.all()

    context = {
        'usuario': usuario,
        'curso': curso,
        'modulos': modulos,
    }

    avaliacao = get_object_or_404(Assessment, pk=id_avaliacao)
    if request.method == 'GET':
        return config_get(request, avaliacao, tipo_pergunta, id_pergunta, context)
    elif request.method == 'POST':
        return config_post(request, avaliacao, tipo_pergunta, id_pergunta, context)


#ANCHOR funções auxiliares
def config_get(request, avaliacao, tipo_pergunta, id_pergunta, context):
    if tipo_pergunta == 'objetiva':
        pergunta = get_object_or_404(PerguntaObjetiva, pk=id_pergunta)
    elif tipo_pergunta == 'discursiva':
        pergunta = get_object_or_404(PerguntaDiscursiva, pk=id_pergunta)
    elif tipo_pergunta == 'check':
        pergunta = get_object_or_404(PerguntaCheck, pk=id_pergunta)
    else:
        return HttpResponseNotFound()

    context.update({
        'avaliacao': avaliacao,
        'tipo_pergunta': tipo_pergunta,
        'pergunta': pergunta,
    })

    return render(
        request,
        'avaliacao.html',
        context
    )


def config_post(request, avaliacao, tipo_pergunta, id_pergunta, context):
    if tipo_pergunta == 'objetiva':
        pergunta = get_object_or_404(PerguntaObjetiva, pk=id_pergunta)
        pergunta.resposta = pergunta.alternativa_set.filter(id=request.POST.get('pergunta_objetiva', None)).first()
        pergunta.marcar_respondida(request.user)
    elif tipo_pergunta == 'discursiva':
        pergunta = get_object_or_404(PerguntaDiscursiva, pk=id_pergunta)
        pergunta.resposta = request.POST.get('pergunta_discursiva', None)
        pergunta.marcar_respondida(request.user)
    elif tipo_pergunta == 'check':
        pergunta = get_object_or_404(PerguntaCheck, pk=id_pergunta)
        pergunta.resposta = request.POST.get('pergunta_check', None)
        pergunta.marcar_respondida(request.user)
    else:
        return HttpResponseNotFound()

    return redirect(reverse_lazy(
        'avaliacao',
        kwargs={
            'id_avaliacao': avaliacao.id,
            'tipo_pergunta': tipo_pergunta,
            'id_pergunta': id_pergunta
        }
    ))
