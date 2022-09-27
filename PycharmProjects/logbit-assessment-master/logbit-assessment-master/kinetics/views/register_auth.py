from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from ..models import Kinetics

# Create your views here.

@csrf_exempt
def register_auth(request):
    # home/register_auth/
    if request.method == "POST":
        request.session['token_auth'] = request.POST.get('token', None)
        request.session['email_auth'] = request.POST.get('email', None)
    else:
        request.session['token_auth'] = None
        request.session['email_auth'] = None
        #request.session['token_auth'] = "61fa71f79b3578306a520592.kIRYCY4w6E9u"
        #request.session['email_auth'] = "dyego.magno@novadata.com.br"
    
    kinetics = Kinetics.objects.first()
    exibir_mensagem = kinetics.buscar_dados_usuario(request)
    
    return redirect('/?mensagem={}'.format(exibir_mensagem))
