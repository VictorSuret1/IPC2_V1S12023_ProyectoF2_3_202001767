from django.shortcuts import render,redirect
from proyecto.fase1.listaEnlazada import ListaEnlazada
from proyecto.fase1.listaDobleCircular import  listaDobleCircular
from proyecto.fase1.cons import Peliculas, Usuario, Salas
from proyecto.fase1.listaDoble import listaDoble

from django.shortcuts import render



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

def default_view(request):
    return render(request, 'principal/Home.html')

def cliente(request):
    return render(request, 'principal/cliente.html')

def administrador(request):
    return render(request, 'principal/admin.html')

def login(request):
    admin()
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        rolUser = lista.login(correo, contrasena)

        if rolUser == 'cliente':
            return redirect('cliente')
        elif rolUser == 'administrador':
            return redirect('administrador')

    return render(request, 'principal/login.html')

    
    
def cargaXMLUsuarios(request):
    if request.method == 'POST':
        lista.CargarXML(1,datos)
    return render(request, 'usuarios/listaUsuarios.html', {'usuario': lista})

def listaUser(request):
    usuario = list(lista)
    return render(request, 'usuarios/listaUsuarios.html', {'usuario': usuario})

def admin():
    rol = 'administrador'
    nombre= 'admin'
    apellido = 'admin'
    telefono = 123123
    correo = 'admin'
    contrasena = 'admin'
    objeto = Usuario(rol,nombre,apellido,telefono,correo,contrasena)
    lista.add(objeto)
    
def crearUser(request):
    if request.method == 'POST':
        
        rol = request.POST.get('rol')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        objeto = Usuario(rol,nombre,apellido,telefono,correo,contrasena) 
        lista.add(objeto)
        lista.GuardarXML(rol,nombre,apellido,telefono,correo,contrasena)
        return redirect('listaUser')
    return render(request, 'usuarios/crearUsuario.html')

def actualizarUser(request, correo):
    usuario = next((usuario for usuario in lista if usuario.correo == correo), None)
    if usuario:
        if request.method == 'POST':
            usuario.rol = request.POST.get('rol')
            usuario.nombre = request.POST.get('nombre')
            usuario.apellido = request.POST.get('apellido')
            usuario.telefono = request.POST.get('telefono')
            usuario.correo = request.POST.get('correo')
            usuario.contrasena = request.POST.get('contrasena')
            lista.EditarUsuario(correo, usuario.rol, usuario.nombre, usuario.apellido, usuario.telefono,
                          usuario.correo, usuario.contrasena)
            return redirect('listaUser')
        return render(request, 'usuarios/actualizarUser.html', {'usuario': usuario})
    return redirect('listaUser')
 
def eliminarUsuario(request, correo):
    lista.EliminarUsuario(correo)
    return redirect('listaUser')

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
        peli = Peliculas(categoria, titulo, director, anio, fecha, hora, imagen, precio)
        listaCir.add(peli)
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
    listaCir.eliminarPelicula(titulo)
    return redirect('listaPeli')

def cargaXMLSalas(request):
    if request.method == 'POST':
        listaDob.cargaSalas(salas)
    return render(request, 'salas/listaSalas.html', {'sala': listaDob})

def listaSalas(request):
    sala = list(listaDob)
    return render(request, 'salas/listaSalas.html', {'salas': sala})

def crearSala(request):
    if request.method == 'POST':
        cine = request.POST.get('cine')
        numero =request.POST.get('numero')
        asientos = request.POST.get('asientos')
        sala = Salas(cine,numero,asientos)
        listaDob.add(sala)
        return redirect('listaSalas')
    return render(request, 'salas/crearSala.html')