#Shift + Alt + O para organizar as importações (vs code)

from django.urls import path
from .views import url_alterar_foto

from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('url_alterar_foto/', url_alterar_foto, name='url_alterar_foto'),
]
