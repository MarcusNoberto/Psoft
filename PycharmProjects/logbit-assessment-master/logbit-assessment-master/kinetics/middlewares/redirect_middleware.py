from django.shortcuts import redirect
from kinetics.models import Kinetics

from ..views import register_auth


class RedirectMiddleware:    
	def __init__(self, get_response=None):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_view(self, request, func, args, kwargs):
		kinetics = Kinetics.objects.first()
		print("Executando")

		if func is not register_auth:
			if 'token_auth' in request.session:
				print("Token encontrado")
			else:
				print("Token não encontrado")
				try:
					return redirect(kinetics.url_redirect)
				except:
					pass

		return None
