from django.conf.urls import url,include
from django.urls import path
from apps.registro.views import registro_view, consulta_view, usuario_edit, usuario_delete


urlpatterns = [
    url(r'^$', registro_view, name= 'crear_registro'),
    path('consu/', consulta_view, name='lista_consulta'),
    path('editar/<int:id_usuario>/', usuario_edit, name='editar_registro'),
    path('eliminar/<int:id_usuario>/', usuario_delete, name='eliminar_registro'),
]