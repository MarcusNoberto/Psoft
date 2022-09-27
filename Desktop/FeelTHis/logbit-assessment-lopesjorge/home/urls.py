#Shift + Alt + O para organizar as importações (vs code)

from django.urls import path
from .views import url_alterar_foto
from .views import logout_kinects
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_kinects, name='logout_kinects'),
    path('url_alterar_foto/', url_alterar_foto, name='url_alterar_foto'),
]
