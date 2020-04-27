from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	domicilio = models.TextField()

	#def __str__(self):
	#	return '{} {}'.format(self.nombre, self.apellidos)
