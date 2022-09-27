from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, Group
from core.models.empresa import Empresa
from crum import get_current_user

class ConfiguracaoAssessment(models.Model):
    """
       Classe ConfiguracaoAssessment implementa as funções relacionadas as configuracões Assessment
    """

    nome = models.CharField(
        max_length=250,
        verbose_name="Nome",
        help_text="Campo Obrigatório"
    )

    descricao = models.TextField(
        verbose_name="Decrição",
        blank=True, null=True
    )

    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Empresa"
    )

    grupos = models.ManyToManyField(
        Group,
        verbose_name=('Grupos'),
        blank=True,
    )

    usuarios = models.ManyToManyField(
        User,
        verbose_name=('Usuários'),
        blank=True,
    )

    data_alteracao = models.DateTimeField(
        verbose_name="Data de Alteração",
        auto_now=True
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    usuario_criacao = models.ForeignKey(
		'auth.User', 
		related_name='%(class)s_requests_created',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)

    usuario_atualizacao = models.ForeignKey(
		'auth.User', 
		related_name='%(class)s_requests_modified',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)

    def gerar_configuracoes(self):

        if self.grupos:
            for grupo in self.grupos.all():
                usuario_grupo = Group.objects.get(name=grupo).user_set.all()
                for usuario in usuario_grupo:
                    self.gerar_assessment(usuario)

        for usuario in self.usuarios.all():
            self.gerar_assessment(usuario)

    def gerar_assessment(self, usuario):
        from assessment.models.assessment import Assessment

        

        for configuracao_etapa in self.configuracaoetapa_set.all():
            for configuracao_pergunta_objetiva in configuracao_etapa.configuracaoperguntaobjetiva_set.all():
                if configuracao_pergunta_objetiva.alternativa_correta is None:
                    return 


        assessment = Assessment.objects.create(
                nome = self.nome,
                descricao = self.descricao,
                usuario = usuario,
                configuracao_assessment = self
            )

        for configuracao_etapa in self.configuracaoetapa_set.all():
            etapa = self.gerar_etapa(configuracao_etapa, assessment)
            for configuracao_anexo in configuracao_etapa.configuracaoanexo_set.all():
                self.gerar_anexo(configuracao_anexo, etapa)
            for configuracao_pergunta_objetiva in configuracao_etapa.configuracaoperguntaobjetiva_set.all():
                self.gerar_pergunta_objetiva(configuracao_pergunta_objetiva,etapa)
            for configuracao_pergunta_discursiva in configuracao_etapa.configuracaoperguntadiscursiva_set.all():
                self.gerar_pergunta_discursiva(configuracao_pergunta_discursiva, etapa)
            for configuracao_pergunta_check in configuracao_etapa.configuracaoperguntacheck_set.all():
                self.gerar_pergunta_check(configuracao_pergunta_check, etapa)

        

        return assessment
    
    def gerar_etapa(self, configuracao_etapa, assessment):
        from assessment.models import Etapa

        etapa = Etapa.objects.create(
            nome = configuracao_etapa.nome,
            descricao = configuracao_etapa.descricao,
            ordem = configuracao_etapa.ordem,
            assessment = assessment
        )

        return etapa

    def gerar_anexo(self, configuracao_anexo, etapa):
        from assessment.models.anexo import Anexo

        anexo = Anexo.objects.create(
            titulo = configuracao_anexo.titulo,
            descricao = configuracao_anexo.descricao,
            etapa = etapa
        )

        return anexo

    def gerar_alternativa(self, configuracao_alternativa, pergunta_objetiva):
        from assessment.models.alternativa import Alternativa
        alternativa = Alternativa.objects.create(
            titulo = configuracao_alternativa.titulo,
            descricao = configuracao_alternativa.descricao,
            pergunta_objetiva = pergunta_objetiva
        )

        return alternativa

    def gerar_pergunta_objetiva(self, configuracao_pergunta_objetiva, etapa):
        from assessment.models.pergunta_objetiva import PerguntaObjetiva

        pergunta_objetiva = PerguntaObjetiva.objects.create(
                titulo = configuracao_pergunta_objetiva.titulo,
                descricao = configuracao_pergunta_objetiva.descricao,
                etapa = etapa
            )
        
        for configuracao_alternativa in configuracao_pergunta_objetiva.configuracaoalternativa_set.all():
            alternativa = self.gerar_alternativa(configuracao_alternativa, pergunta_objetiva)
            if(configuracao_alternativa.titulo == configuracao_pergunta_objetiva.alternativa_correta.titulo and alternativa.titulo == configuracao_pergunta_objetiva.alternativa_correta.titulo):
                #arrumar
                pergunta_objetiva.alternativa_correta = alternativa
                pergunta_objetiva.save()
                

        return pergunta_objetiva    





    def gerar_pergunta_discursiva(self,configuracao_pergunta_discursiva, etapa):
        from assessment.models.pergunta_discursiva import PerguntaDiscursiva

        pergunta_discursiva = PerguntaDiscursiva.objects.create(
            titulo = configuracao_pergunta_discursiva.titulo,
            descricao = configuracao_pergunta_discursiva.descricao,
            etapa = etapa,
        )

        return pergunta_discursiva

    def gerar_pergunta_check(self, configuracao_pergunta_check, etapa):
        from assessment.models.pergunta_check import PerguntaCheck

        pergunta_check = PerguntaCheck.objects.create(
            titulo = configuracao_pergunta_check.titulo,
            descricao = configuracao_pergunta_check.descricao,
            resposta_esperada = configuracao_pergunta_check.resposta_esperada,
            etapa = etapa
        )

        return pergunta_check

    def __str__(self):
       return self.nome

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(ConfiguracaoAssessment, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "configuracao_assessment"
        verbose_name = "Configuração Assessment"
        verbose_name_plural = "Configurações Assessment"