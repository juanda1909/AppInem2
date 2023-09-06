from django.db import models

class Estudiante(models.Model):
    Tarjeta_identidad = models.CharField(max_length=20)
    Clave = models.CharField(max_length=100)

    def __str__(self):
        return self.Tarjeta_identidad

class Profesor(models.Model):
    Cedula = models.CharField(max_length=20)
    Clave = models.CharField(max_length=100)

    def __str__(self):
        return self.Cedula
