from django.contrib import admin
from apps.dispositivos.models import Dispositivo
from apps.personas.models import Usuario

# Register your models here.
admin.site.register(Dispositivo)

#def formfield_for_foreignkey(self, db_field, request, **kwargs):
#        if db_field.name == 'usuario':
#            kwargs['queryset'] = Usuario.objects.filter(nombre_apellido='berto')
#        return super(ConsumerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)