import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import models
from decouple import config


class Kinetics(models.Model):
    '''
    Classe para desempenhar as funcionalidades relacionadas a autenticação do usuário.
    Autenticação essa que é feita por uma API.
    '''
    name = models.CharField(
        verbose_name="Nome",
        max_length=100
    )

    description = models.TextField(
        verbose_name="Descrição"
    )

    project_id = models.CharField(
        verbose_name="Id do projeto",
        max_length=100, 
        blank=True, null=True
    )

    secret = models.CharField(
        verbose_name="Secret",
        max_length=255, 
        blank=True, null=True
    )

    project_url = models.URLField(
        verbose_name="URL do projeto",
        blank=True, null=True
    )
        
    url_base = models.URLField(
        verbose_name="URL Base",
        blank=True, null=True
    )

    url_api = models.URLField(
        verbose_name="URL da API",
        blank=True, null=True
    )

    url_redirect = models.URLField(
        verbose_name="URL de Redirect",
        blank=True, null=True
    )
    
    created_at = models.DateTimeField(
        verbose_name="Criado em",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name="Atualizado em",
        auto_now=True
    )
    
    def buscar_dados_usuario(self, request):
        import requests

        try:
            url = self.url_api
            data = {
                'act': 'apiGetUserInfo',
                'secret': self.secret,
                'project': self.project_id,
                'email': request.session['email_auth'],
                'token': request.session['token_auth'],
            }

            requisicao = requests.post(url, data = data)
            request.session['dados_usuario'] = json.loads(requisicao.text)['data']
            """ {
                '_id': {'$oid': '61c236943d0ba93b2f503382'}, 
                'name': 'Dyego Magno', 
                'email': 'dyego.magno@novadata.com.br', 
                'bu': 'SLBU', 
                'fabricante': 10000, 
                'franquiaName': None, 
                'franquia': None, 
                'fabricanteName': 'Embol Bolivia', 
                'project': {
                    'projectId': 'b2b-latam-ou', 
                    'level': '100', 
                    'enabled': 1, 
                    'admin': 10, 
                    'last_login': 1643803367, 
                    'session_token': '61fa72e68f4cfa45c03eec94.l7v6xuQaqs40', 
                    'customChecks': [
                        'skipper'
                    ], 
                    'multibufabs': [
                        1, 3, 7, 9
                    ]
                }, 
                'info-fabricante': {
                    'code': 53, 
                    'name': 'EMBOL Bolívia', 
                    'tier': 1, 
                    'zone-code': 301, 
                    'zone-name': 'South - South Latin', 
                    'group-code': 305, 
                    'group-name': 'SIN GRUPO', 
                    'auth-zone-name': 'SLBU', 
                    'auth-name': 'Embol Bolivia', 
                    'auth-code': 10000
                }
            } """
            
            return self.logar_usuario(request)
        except:
            print("Erro ao buscar dados do usuário")

    def logar_usuario(self, request):
        email = request.session['dados_usuario'].get('email')
        permissions = request.session['dados_usuario'].get('project').get('customChecks')
        name = request.session['dados_usuario'].get('name')
        default_password = config('DEFAULT_PASSWORD')
        try:
            user=User.objects.get(
                username=email
            )
            exibir_mensagem_boas_vindas = False

        except:
            user=User.objects.create_user(
                username=email,
                email=email,
                password=default_password
            )
            exibir_mensagem_boas_vindas = True

        if not user.first_name and user.first_name != name:
            name_dividido = name.split(' ')
            try:
                user.first_name = name_dividido[0]
            except:
                pass

            try:
                if len(name_dividido)>1:
                    user.last_name = name_dividido[len(name_dividido)-1]
            except:
                pass

        if not user.is_superuser and 'skipper' in permissions:
            user.is_superuser = True
            user.is_staff = True

        user.save()

        user_final = authenticate(username=user.username, password=default_password)
        login(request, user_final)

        if user_final is not None:
            print("Usuário autenticado")
        else:
            print("Usuário não autenticado")

        return exibir_mensagem_boas_vindas
    
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'kinetics'
        verbose_name = "Kinetic"
        verbose_name_plural = "Kinetics"
