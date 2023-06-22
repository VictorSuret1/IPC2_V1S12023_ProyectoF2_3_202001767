from django.shortcuts import render,redirect
from proyecto.fase1.listaEnlazada import ListaEnlazada
from proyecto.fase1.listaDobleCircular import  listaDobleCircular
from proyecto.fase1.listaDoble import listaDoble

# Create your views here.
global lista
lista = ListaEnlazada()
global listaCir
listaCir = listaDobleCircular()
global listaDob
listaDob = listaDoble()
global datos
datos = 'datos.xml'
global pelis
pelis = 'peliculas.xml'
global salas
salas = 'salas.xml'

def listaUser(request):
    lista.CargarXML(1,datos)
    
    return render(request, 'usuarios/listaUsuarios.html', {'usuarios': lista})


def crearUser(request):
    if request.method == 'POST':
        
        rol = request.POST.get('rol')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        objeto = {'rol':rol,'nombre':nombre,'apellido':apellido,'telefono':telefono,'correo':correo,'contrasena':contrasena}
        lista.add(objeto)

        return redirect('listaUser')
    return render(request, 'usuarios/crearUsuario.html')

def actualizarUser(request, correo):
    usuario = next((usuario for usuario in lista if usuario['correo'] == correo), None)
    if usuario:
        if request.method == 'POST':
            usuario['rol'] = request.POST.get('rol')
            usuario['nombre'] = request.POST.get('nombre')
            usuario['apellido'] = request.POST.get('apellido')
            usuario['telefono'] = request.POST.get('telefono')
            usuario['correo'] = request.POST.get('correo')
            usuario['contrasena'] = request.POST.get('contrasena')
            return redirect('listaUser')
        return render(request, 'usuarios/actualizarUser.html', {'usuario': usuario})
    return redirect('listaUser')
    
def eliminarUser(request, correo):
    pass

def listaPeli(request):
    peliculas = list(listaCir)
    return render(request, 'peliculas/listaPeliculas.html', {'peliculas': peliculas})

def cargaXML(request):
    if request.method == 'POST':
        listaCir.CargarPelis(pelis)
    return render(request, 'peliculas/listaPeliculas.html', {'peliculas': listaCir})

def crearPeli(request):
    if request.method == 'POST':
        
        categoria = request.POST.get('categoria')
        titulo = request.POST.get('titulo')
        director = request.POST.get('director')
        anio = request.POST.get('anio')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        imagen = request.POST.get('imagen')
        precio = request.POST.get('precio')
        objeto = {'categoria':categoria,'titulo':titulo,'director':director,'anio':anio,'fecha':fecha,'hora':hora, 'imagen':imagen, 'precio':precio}
        listaCir.add(objeto)
    
        return redirect('listaPeli')
    return render(request, 'peliculas/crearPelicula.html')

def actualizarPeli(request, titulo):
    peli = next((peli for peli in listaCir if peli.titulo == titulo), None)
    if peli:
        if request.method == 'POST':
            peli.categoria = request.POST.get('categoria')
            peli.titulo = request.POST.get('titulo')
            peli.director = request.POST.get('director')
            peli.anio = request.POST.get('anio')
            peli.fecha = request.POST.get('fecha')
            peli.hora = request.POST.get('hora')
            peli.imagen = request.POST.get('imagen')
            peli.precio = request.POST.get('precio')
            return redirect('listaPeli')
        return render(request, 'peliculas/actualizarPeli.html', {'peli': peli})
    return redirect('listaPeli')


def eliminarPeli(request, titulo):
    
    listaCir.remove(titulo)
    return redirect('listaPeli')