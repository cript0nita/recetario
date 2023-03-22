from django.db import models

# Create your models here.

class Categoria(models.Model):   
    """
    Modelo de datos de la tabla recetas_categoria
    """ 
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    """
    Modelo de datos de la tabla recetas_receta
    """

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    dificultad = models.CharField(max_length=255, blank=True, null=True)
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
