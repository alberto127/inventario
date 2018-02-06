from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from apps.personas.models import Usuario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.personas.forms import UsuarioForm

# Create your views here.

class UsuariosList(ListView):
	model=Usuario
	template_name='personas/personas_list.html'


def usuario_nuevo(request):
	model=Usuario
	template_name='personas/personas_form.html'
	form=UsuarioForm
#	context={}
#	return render(request, 'personas/personas_add.html', context)
	success_url=reverse_lazy('usuarios:usuario_listar')


def add_usuario(request):
	if request.method=='POST':
		form=UsuarioForm(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
		#	dispositivo=DispositivoForm.save(commit=False)
		#	dispositivo.dispositivo=request.tipo_dispositivo
		#	dispositivo.num_serie=request.num_serie
		#	dispositivo.marca=request.marca
		#	dispositivo.modelo=request.modelo
		#	dispositivo.fecha_instalacion=request.fecha_instalacion
		#	dispositivo.usuario=request.asignar_usuario
			user.save()
			return HttpResponseRedirect(reverse_lazy('usuarios:usuario_listar'))
		else:
			return render(request, 'personas/personas_add.html', {'form' : form})
		#	return HttpResponse("Error en el envio/guardado")

	else:
		form=UsuarioForm()
		context={}
		return render(request, 'personas/personas_add.html', context)
#	def POST(request):
#		if request.method=='POST':
#			if form.is_valid():
#				form.save()
#			return HttpResponseRedirect(self.get_success_url())
#class UsuariosCreate(CreateView):
#	model=Usuario
#	form_class=UsuarioForm
#	template_name='personas/personas_form.html'
#	success_url=reverse_lazy('usuarios:usuario_listar')

    #def get_form_kwargs(self):
    #   kwargs = super().get_form_kwargs()
    #   kwargs.update({'request': self.request})
    #   return kwargs