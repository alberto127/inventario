# -*- encoding:utf-8 -*-
from django import forms
from apps.dispositivos.models import Dispositivo
from apps.personas.models import Usuario


FC = (
	('No', 'NO'),
	('Si', 'SI'),
)
    
	
class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields=['usuario','departamento','email','fuera_convenio']

	#def __init__(self, request, *args, **kwargs):
    #	super().__init__(*args, **kwargs)
    #    self.fields['usuario'].queryset =  usuario.objects.filter(user=request.user)

	#class Meta:
	#	model = Usuario
	#	fields = [
	#		'nombre_apellido',
	#		'departamento',
	#		'email',
	#		'fuera_convenio',

		
	#	]
	#	labels = {
	#		'nombre_apellido': 'Usuario',
	#		'departamento': 'Dpto.',
	#		'email': 'Email',
	#		'fuera_convenio': 'Fuera de convenio',


	#	}
	#	widgets = {
	#		'nombre_apellido':forms.TextInput(attrs={'class':'form-control'}),
	#		'departamento':forms.TextInput(attrs={'class':'form-control'}),
	#		'email':forms.TextInput(attrs={'class':'form-control'}),
	#		'fuera_convenio':forms.Select(choices=FC),

	#		}
		

