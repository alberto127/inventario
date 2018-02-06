
from django.conf.urls import url, include
from apps.personas.views import UsuariosList, add_usuario
from . import views

urlpatterns = [

   url(r'^listar$', UsuariosList.as_view(), name='usuario_listar'),
   url(r'^nuevo$', views.add_usuario, name='usuario_crear'),
   #url(r'^nuevo/add$', views.add_usuario, name='add_usuario'),
   #url(r'^solicitud/editar/(?P<pk>\d+)$', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
   #url(r'^solicitud/eliminar/(?P<pk>\d+)$', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
]