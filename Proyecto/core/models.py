from django.db import models

# Crear Modelos
class Mueble(models.Model):
    muebleElegido=(
        ('mesa','Mesa'),
        ('silla','Silla'),
        ('alacena','Alacena'),
        ('cama','Cama'),
        ('sillon','Sillon'),
        ('escritorio','Escritorio'),
        ('otro','Otro'),
    )
    titulo=models.CharField(max_length=150)
    def __str__(self):
        return self.titulo


