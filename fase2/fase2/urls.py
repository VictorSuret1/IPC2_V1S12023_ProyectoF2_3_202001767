"""
URL configuration for fase2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto.views import default_view, login, cliente, administrador
from proyecto.views import listaUser,crearUser,cargaXMLUsuarios,actualizarUser,eliminarUsuario,listaPeli,crearPeli,cargaXML, actualizarPeli, eliminarPeli,listaSalas
from proyecto.views import cargaXMLSalas, crearSala, actualizarSalas, eliminarSalas ,cargalistaCliente
urlpatterns = [
    path('', default_view, name='default'),
    path('login/' ,login, name='login' ),
    path('cliente/', cliente, name ='cliente'),
    path('administrador/', administrador, name= 'administrador'),

    path('admin/', admin.site.urls),
    path('usuarios/', listaUser, name = 'listaUser'),
    path('usuarios/crear/', crearUser, name = 'crearUsuario'),
    path('usuarios/carga-xml/',cargaXMLUsuarios, name = 'cargaXMLUsuarios' ),
    path('usuarios/actualizar/<str:correo>', actualizarUser, name='actualizarUser'),
    path('usuarios/eliminarUsuario/<str:correo>', eliminarUsuario, name="eliminarUsuario"),

    path('cliente/cargalistaCliente',cargalistaCliente,name='cargalistaCliente'),

    


    path('peliculas/', listaPeli, name = 'listaPeli'),
    path('peliculas/crearPelicula/', crearPeli, name = 'crearPelicula' ),
    path('peliculas/cargar-xml/', cargaXML, name='cargaXML'),
    path('peliculas/actualizarPeli/<str:titulo>', actualizarPeli, name='actualizarPeli'),
    path('peliculas/eliminarPeli/<str:titulo>', eliminarPeli, name='eliminarPeli'),

    path('salas/', listaSalas,name='listaSalas' ),
    path('salas/carga/',cargaXMLSalas, name='cargaXMLSalas'),
    path('salas/crearSala/', crearSala, name='crearSala'),
    path('salas/actualizarSalas/<str:numero>', actualizarSalas, name='actualizarSalas'),
    path('salas/eliminarSalas/<str:numero>',eliminarSalas,name='eliminarSalas' )
]
