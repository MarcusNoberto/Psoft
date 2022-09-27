'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logbit_assessment.settings')

application = Cling(get_wsgi_application())