from django.contrib import admin
from .models import *

# Registra tus modelos.
admin.site.register(Mueble)
admin.site.register(Avatar)
admin.site.register(Comentario)
admin.site.register(Carrito)
