from django.shortcuts import render
# Crear vistas.
def inicio(request):
    return render(request,'core/inicio.html')