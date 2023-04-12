from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from core.views import home,register,login_request,editarPerfil,about,contacto,agregar_producto, eliminar_producto, restar_producto, limpiar_carrito,comprar
from core.views import MuebleCreateView,MuebleDeleteView,MuebleDetailView,MuebleUpdateView,HomeView,ProductosListView

urlpatterns = [
    path('home/',home,name="home"),
    path('',HomeView.as_view() ,name="inicio"),
    path('register/',register ,name='Register'),
    path('login/',login_request ,name='Login'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='Logout'),
    path('editarPerfil', editarPerfil, name="EditarPerfil"), 
    path('acercaDeMi/', about, name='acercaDM'),
    path('contacto/', contacto, name='contacto'),
    path('comprar/',comprar, name='comprar'),

    #CARRITO
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="Limpiar"),

]

#URL de vistas basadas en clases
urlpatterns +=[
    path('productos/list/',ProductosListView.as_view(),name='productos'),
    path('<pk>',MuebleDetailView.as_view(),name='Detail'),
    path('nuevo/',MuebleCreateView.as_view(),name='New'),
    path('editar/<pk>/',MuebleUpdateView.as_view(),name='Edit'),
    path('borrar/<pk>/',MuebleDeleteView.as_view(),name='Delete'),
]