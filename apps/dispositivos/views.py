from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from apps.dispositivos.models import Dispositivo
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from apps.dispositivos.forms import DispositivoForm
from apps.personas.forms import UsuarioForm
from apps.personas.models import Usuario
from django.core import serializers
from django.forms.models import model_to_dict


# Create your views here.
def index_dispositivos(request):
	return HttpResponse("Soy la aplicacion dispositivos")

class DispositivosList(ListView):
	model=Dispositivo
	template_name='dispositivos/dispositivos_list.html'
	context_object_name='dispositivos'

#class BusquedaView(ListView):
#	model=Dispositivo
#	template_name='dispositivos/busqueda.html'
#	context_object_name='dispositivos'

#class BusquedaAjaxView(TemplateView):
#
#	def get(self,request,*args,**kwargs):
#		dispo=request.GET['dispos']
#		dispositivos=Dispositivo.objects.filter(dispositivo=dispo)
#		data =serializers.serialize('json', dispositivos, fields=('dispositivo',
#			'marca','modelo','num_serie','fecha_instalacion','usuario'))
#		return HttpResponse(data, mimetype='application/json')

#class DispositivosCreate(CreateView):
#	model=Dispositivo
#	form_class=DispositivoForm
#	template_name='dispositivos/dispositivos_form.html'
#	success_url=reverse_lazy('dispositivos:dispositivo_listar')

    #def get_form_kwargs(self):
    #   kwargs = super().get_form_kwargs()
    #   kwargs.update({'request': self.request})
    #   return kwargs
import json
def mostrarUser(request):

	usuario=request.GET.get('user')  #diccionario
	usuario_asignado=Usuario.objects.filter(usuario=usuario)
	data=serializers.serialize('json', usuario_asignado, fields=('departamento','email'))
	#usuarios=[usuario_serializer(usuario) for usuario in usuarios]
	#return HttpResponse(json.dumps(usuarios), content_type="application/json")
	#print (type(usuario_asignado))
	#print (type(model_to_dict(usuario_asignado)))
	return HttpResponse(data, content_type="application/json")

#def usuario_serializer(usuario):
#	return {'usuario': usuario.usuario, 'departamento': usuario.departamento}





def dispositivo_nuevo(request):


	if request.method=='POST':
		dispositivo = request.POST.get('tipo_dispositivo', None)
		marca = request.POST.get('marca', None)
		modelo = request.POST.get('modelo', None)
		num_serie = request.POST.get('num_serie', None)
		fecha_instalacion = request.POST.get('fecha_instalacion', None)
		usuario = request.POST.get('asignar_usuario', None)

		if usuario=="Almacen":
# https://es.stackoverflow.com/questions/17426/c%C3%B3mo-puedo-saber-si-un-queryset-de-django-est%C3%A1-vac%C3%ADo/25239
			try:
				user = Usuario.objects.get(usuario="Almacen")
			except Usuario.DoesNotExist:   
				# entrará aqui cuando no exista ningun elemento que coincida con la busqueda
				u=Usuario(usuario='Almacen',departamento='Informatica', email='informatica@apvigo.es', fuera_convenio='No')
				u.save()			
		
		try:
			dispositivo_nuevo= Dispositivo(dispositivo = dispositivo, marca = marca, modelo = modelo, num_serie = num_serie, fecha_instalacion = fecha_instalacion, usuario = usuario)
			dispositivo_nuevo.save()
			return HttpResponseRedirect(reverse_lazy('dispositivos:dispositivo_listar'))
			#return render(request, 'personas/personas_list.html')
			#return HttpResponse(json.dumps({"mensaje": "Usuario guardado exitosamente."}), content_type='application/json')
			#return HttpResponseRedirect(reverse_lazy('personas:usuario_listar'), json.dumps({"mensaje": "Usuario guardado exitosamente."}), content_type='application/json')
		except:
			return HttpResponseRedirect(reverse_lazy('dispositivos:dispositivo_listar'))
			#return HttpResponse(json.dumps({"mensaje": "ERROR"}), content_type='application/json')
	else:
		form=DispositivoForm()
		return render(request, 'dispositivos/dispositivos_form.html')


########################################         ANTIGUO         ########################
#	if request.method=='POST':
#		dispo=DispositivoForm(request.POST)
#
#		if request.POST.get('asignar_usuario')=='sin_asignar':
#			user='almacen11'
#			user_almacen=Usuario.objects.filter(usuario=user)
#			if user_almacen != 'almacen11':
#				u=Usuario(usuario='almacen11',departamento='Informatica', email='Informatica@apvigo.es', fuera_convenio='False')
#				u.save()
#				dispo=Dispositivo(request.POST.get('tipo_dispositivo'),
#					request.POST.get('marca'),
#					request.POST.get('modelo'),
#					request.POST.get('num_serie'),
#					request.POST.get('fecha_instalacion'),
#					user)
#
#				dispo.save()
#				return HttpResponseRedirect(reverse_lazy('dispositivos:dispositivo_listar'))
#			else:
#			
#				dispo=Dispositivo(request.POST.get('tipo_dispositivo'),
#					request.POST.get('marca'),
#					request.POST.get('modelo'),
#					request.POST.get('num_serie'),
#					request.POST.get('fecha_instalacion'),
#					user)
#
#		else:
#			dispo=Dispositivo(request.POST.get('tipo_dispositivo'),
#				request.POST.get('marca'),
#				request.POST.get('modelo'),
#				request.POST.get('num_serie'),
#				request.POST.get('fecha_instalacion'),
#				request.POST.get('asignar_usuario'))
#
#			dispo.save()
#			return HttpResponseRedirect(reverse_lazy('dispositivos:dispositivo_listar'))
#
#	else:
#		form=DispositivoForm()
#		usuario = Usuario.objects.all()
#		return render(request, 'dispositivos/dispositivos_form.html', {'usuario' : usuario})






#class DispositivosCreate(CreateView):
#	model=Dispositivo
#	template_name='dispositivos/dispositivos_form.html'
#	form_class=DispositivoForm
#	second_form_class=UsuarioForm
#	success_url=reverse_lazy('dispositivos:dispositivo_listar')
#
#	def get_context_data(self, **kwargs):
#		context=super(DispositivosCreate, self).get_context_data(**kwargs)
#		if 'form' not in context:
#			context['form']=self.form_class(self.request.GET)
#		if 'form2' not in context:
#			context['form2']=self.second_form_class(self.request.GET)
#		return context
#
#	def post(self,request, *args, **kwargs):
#		self.object=self.get_object
#		form=self.form_class(request.POST)
#		form2=self.second_form_class(request.POST)
#		if form.is_valid() and form2.is_valid():
#			asignacion=form.save(commit=False)
#			asignacion.usuario=form2.save()
#			asignacion.save()
#			return HttpResponseRedirect(self.get_success_url())
#		else:
#			return self.render_to_response(self.get_context_data(form=form, form2=form2))