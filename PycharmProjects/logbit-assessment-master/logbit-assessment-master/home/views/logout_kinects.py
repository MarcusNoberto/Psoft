from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout


def logout_kinects(request):

    logout(request)
    try:
        request.session.pop('token_auth')
    except:
        pass
    try:
        request.session.pop('email_auth')
    except:
        pass
    try:
        request.session.pop('dados_usuario')
    except:
        pass
    
    return redirect(reverse_lazy('home'))


    
