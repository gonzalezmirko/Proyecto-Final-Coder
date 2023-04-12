from django.db import models
from django.contrib.auth.models import User

# Crear Modelos
class Mueble(models.Model):
    nombre=models.CharField(max_length=40)
    modelo=models.CharField(max_length=150)
    descripcion=models.CharField(max_length=250)
    precio=models.FloatField(default='')
    imagen=models.ImageField(null=True, blank=True, upload_to="static\core\images\\media")
    oferta=models.BooleanField(default='False')
    def __str__(self):
        return f"{self.id} - {self.nombre}"

class Avatar(models.Model):
    #vinculo con usuario
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares de media
    imagen=models.ImageField(upload_to='avatares',null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Comentario(models.Model):
    comentario = models.ForeignKey(Mueble, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)

class Carrito(models.Model):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": float(producto.precio),
                "acumulado": float(producto.precio),
                "imagen":producto.imagen.url,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio"] = producto.precio
            self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["precio"] = producto.precio
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()
        

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
    
    
    


