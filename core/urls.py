from django.urls import path
from .views import colaborador, home, vercolaborador, form_del_colaborador, form_mod_colaborador

urlpatterns = [
    path('', home,name="home"),
    path('colaborador/', colaborador, name='colaborador'),
    path('vercolaborador/', vercolaborador, name='vercolaborador'),
    path('form_mod_colaborador/<id>', form_mod_colaborador, name="form_mod_colaborador"),
    path('form_del_colaborador/<id>', form_del_colaborador, name="form_del_colaborador") 
]