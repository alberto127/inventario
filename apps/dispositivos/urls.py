

from django.conf.urls import url, include
from apps.dispositivos.views import index_dispositivos, DispositivosList, mostrarUser, add_dispositivo
from . import views

urlpatterns = [
   url(r'^index$', index_dispositivos),
   url(r'^listar$', DispositivosList.as_view(), name='dispositivo_listar'),
   url(r'^nuevo$', views.add_dispositivo, name='dispositivo_crear'),
   url(r'^muestra_usuario$', views.mostrarUser, name='muestra_usuario'),
   
    #YOUTUBE Tutorial N° 15 Django 1.5: Ajax
  # url(r'^busqueda$', views.BusquedaView.as_view(),name='busqueda'),
  # url(r'busqueda_ajax/$', BusquedaAjaxView.as_view()),

   #YOUTUBE Tutorial N° 15 Django 1.5: Ajax
	#END
   #url(r'^solicitud/editar/(?P<pk>\d+)$', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
   #url(r'^solicitud/eliminar/(?P<pk>\d+)$', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
]
