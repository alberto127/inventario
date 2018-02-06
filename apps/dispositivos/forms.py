# -*- encoding:utf-8 -*-
from django.forms import ModelForm
from apps.dispositivos.models import Dispositivo
from apps.personas.models import Usuario



class DispositivoForm(ModelForm):
    # TODO: Define form fields here
    class Meta:
        model = Dispositivo
        fields=['dispositivo','marca','modelo','num_serie','fecha_instalacion','usuario']

#class DispositivoFormVIEJO(ModelForm):

	#def __init__(self, request, *args, **kwargs):
    #	super().__init__(*args, **kwargs)
    #    self.fields['usuario'].queryset =  usuario.objects.filter(user=request.user)

#	class Meta:
#		model = Dispositivo
#		fields = [
#			'dispositivo',
#			'marca',
#			'modelo',
#			'num_serie',
#			'fecha_instalacion',
#			'usuario',
#		
#		]
#		labels = {
#			'dispositivo': 'Dispositivo',
#			'marca': 'Marca',
#			'modelo': 'Modelo',
#			'num_serie': 'Numero de serie',
#			'fecha_instalacion': 'Fecha asignación',
#			'usuario': 'Usuario asignado',
#
#		}
#		widgets = {
#			'dispositivo':forms.TextInput(attrs={'class':'form-control'}),
#			'marca':forms.TextInput(attrs={'class':'form-control'}),
#			'modelo':forms.TextInput(attrs={'class':'form-control'}),
#			'num_serie':forms.TextInput(attrs={'class':'form-control'}),
#			'fecha_instalacion':forms.DateInput(attrs={'type':'date'}),
#			'usuario':forms.Select(attrs={'class':'form-control'}),
#			#'usuario':forms.ModelChoiceField(queryset=Usuario.objects.all(),to_field_name='nombre_apellido'),
#}
		

