from django.db import models

# Create your models here.


#FC = (
#	(True, 'SI'),
#	(False, 'NO'),
#)
    
class Usuario(models.Model):
	usuario=models.CharField(primary_key=True, max_length=30)
	departamento=models.CharField(max_length=40, blank=True)
	email=models.EmailField(blank=True)
	fuera_convenio=models.BooleanField(blank=True)

	def __str__(self):
		return '{}'.format(self.usuario)