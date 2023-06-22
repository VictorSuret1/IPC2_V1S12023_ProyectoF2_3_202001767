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
from proyecto.views import listaUser,crearUser,cargaXMLUsuarios,actualizarUser,eliminarUser,listaPeli,crearPeli,cargaXML, actualizarPeli, eliminarPeli

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', listaUser, name = 'listaUser'),
    path('usuarios/crear/', crearUser, name = 'crearUsuario'),
    path('usuarios/carga-xml',cargaXMLUsuarios, name = 'cargaXMLUsuarios' ),
    path('usuarios/actualizar/<str:correo>', actualizarUser, name='actualizarUser'),
    path('usuarios/eliminar/<str:correo>', eliminarUser, name="eliminarUser"),

    path('peliculas/', listaPeli, name = 'listaPeli'),
    path('peliculas/crearPelicula/', crearPeli, name = 'crearPelicula' ),
    path('peliculas/cargar-xml', cargaXML, name='cargaXML'),
    path('peliculas/actualizarPeli/<str:titulo>', actualizarPeli, name='actualizarPeli'),
    path('peliculas/eliminarPeli/<str:titulo>', eliminarPeli, name='eliminarPeli')
]
