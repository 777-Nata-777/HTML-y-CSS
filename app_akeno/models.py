from django.db import models

# Create your models here.
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Anime(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    portada = models.ImageField(upload_to='portadas/')
    portada_grande = models.ImageField(upload_to='portadas_grandes/')
    etiquetas = models.ManyToManyField(Etiqueta)

    def __str__(self):
        return self.nombre

class Temporada(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return f"Temporada {self.numero} de {self.anime.nombre}"

class Episodio(models.Model):
    temporada    = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    nombre       = models.CharField(max_length=200, blank=True)
    video        = models.FileField(upload_to='videos/', blank=True, null=True)
    portada_ep   = models.ImageField(upload_to='portadas_episodios/', blank=True, null=True)
