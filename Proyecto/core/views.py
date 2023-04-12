from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from core.forms import UserRegisterForm,UserEditForm,FormNuevoMueble
from django.contrib.auth.decorators import login_required

from core.models import Mueble,Carrito
from django.views.generic import ListView,TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Crear vistas.
#@login_required
def home(request):
    return render(request,'core/padre.html')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/inicio.html'
    login_url=reverse_lazy('home')

def contacto(request):
    return render(request,'core/contacto.html') 

def about(request):
    return render(request, 'core/acercaDeMi.html', {})

def register(request):
      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"core/inicio.html" ,  {"mensaje":"Usuario Creado :)"})


      else:
            form = UserRegisterForm()     

      return render(request,"core/registro.html" ,  {"form":form})

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "core/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "core/login.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "core/login.html", {"form":form})

    form = AuthenticationForm()

    return render(request, "core/login.html", {"form": form})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "core/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "core/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

@login_required
def comprar(request):
    return render(request,'core/comprar.html')

class ProductosListView(ListView):
    model = Mueble
    template_name='core/productos.html'


#Clases basadas en vistas
#class MuebleListView(ListView):
    #model = Mueble
    #template_name='core/mueble_list.html'
    #def get(self,request,*args, **kwargs):
        #print("\n\n\nMI PRINT\n\n\n")
        #return super().get(self,request,*args, **kwargs)

class MuebleDetailView(DetailView):
    model = Mueble
    template_name='core/mueble_detalle.html'

class MuebleCreateView(CreateView):
    model = Mueble
    template_name='core/agregar_mueble.html'
    fields=['nombre','modelo','descripcion','precio','imagen','oferta']
    success_url='/core/productos/list'
    


class MuebleUpdateView(UpdateView):
    model = Mueble
    success_url='/core/productos/list'
    fields=['nombre','modelo','descripcion','precio','imagen','oferta']

class MuebleDeleteView(DeleteView):
    model = Mueble
    success_url='/core/productos/list'

#Carrito

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Mueble.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("productos")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Mueble.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("productos")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Mueble.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("productos")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("comprar")
