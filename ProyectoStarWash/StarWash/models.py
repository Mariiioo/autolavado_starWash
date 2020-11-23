from django.db import models

# Create your models here.

class Galeria(models.Model):
    nombre=models.CharField(max_length=60,primary_key=True)
    descripcion=models.TextField()
    imagen=models.ImageField(upload_to='galeria',null=True)

    def __str__(self):
        return self.nombre

class Slider(models.Model):
    nombre=models.CharField(max_length=60,primary_key=True)
    imagen=models.ImageField(upload_to='slider',null=True)
    
    def __str__(self):
        return self.nombre

class Insumo (models.Model):
    nombre = models.CharField(max_length=80, primary_key=True)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=200, null=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class MisionVision(models.Model):
    nombre=models.CharField(max_length=60,primary_key=True)
    mision = models.TextField()
    imagenMision=models.ImageField(upload_to='misionVision',null=True)
    vision = models.TextField()
    imagenVision=models.ImageField(upload_to='misionVision',null=True)

    def __str__(self):
        return self.nombre    

class Contacto (models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    apellido = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50,null=True)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre