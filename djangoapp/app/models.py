from django.db import models

class Mercado(models.Model):

    titulo = models.TextField()
    precio = models.TextField()
    envio = models.TextField()
    vendido = models.TextField()
    opiniones = models.TextField()
