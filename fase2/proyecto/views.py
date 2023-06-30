from django.shortcuts import render,redirect
from proyecto.fase1.listaEnlazada import ListaEnlazada
from proyecto.fase1.listaDobleCircular import  listaDobleCircular
from proyecto.fase1.listaDobleTarjetas import listaDobleTarjeta
from proyecto.fase1.cons import Peliculas, Usuario, Salas,Tarjetas
from proyecto.fase1.listaDoble import listaDoble
import xml.etree.ElementTree as ET
import requests
import json

from django.shortcuts import render

rol = 'administrador'
nombre= 'admin'
apellido = 'admin'
telefono = 123123
correo = 'admin'
contrasena = 'admin'


# Create your views here.
global lista
lista = ListaEnlazada()
objeto = Usuario(rol,nombre,apellido,telefono,correo,contrasena)
lista.add(objeto)
global listaCir
listaCir = listaDobleCircular()
global listaDob
listaDob = listaDoble()
global listTar
listTar = listaDobleTarjeta()
global datos
datos = 'datos.xml'
global pelis
pelis = 'peliculas.xml'
global salas
salas = 'salas.xml'
global favs
favs = []




def default_view(request):
    peli = cargarPeliculasDesdeXML()
    return render(request, 'principal/Home.html', {'peli':peli})

def cliente(request):
    return render(request, 'principal/cliente.html')

def administrador(request):
    return render(request, 'principal/admin.html')



def login(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        rolUser = lista.login(correo, contrasena)

        if rolUser == 'cliente':
            return redirect('cargalistaCliente')
        elif rolUser == 'administrador':
            return redirect('administrador')

    return render(request, 'principal/login.html')

    
def cargaXMLUsuarios(request):
    if request.method == 'POST':
        lista.CargarXML(1)

        response = requests.get('http://localhost:5007/getUsuarios')
        usuariosAPI = response.json()
        print(usuariosAPI)

        for usuario in usuariosAPI["usuario"]:
            rol = usuario["rol"]
            nombre = usuario["nombre"]
            apellido = usuario["apellido"]
            telefono = usuario["telefono"]
            correo = usuario["correo"]
            contrasena = usuario["contrasena"]
            objeto = Usuario(rol, nombre, apellido, telefono, correo, contrasena)
            lista.add(objeto)


        return redirect('listaUser')
    return render(request, 'usuarios/listaUsuarios.html', {'usuario': lista})

def listaUser(request):
    usuario = list(lista)
    return render(request, 'usuarios/listaUsuarios.html', {'usuario': usuario})


    
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

def registraCliente(request):
    if request.method == 'POST':
        rol ='usuario'
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        objeto = Usuario(rol,nombre,apellido,telefono,correo,contrasena) 
        lista.add(objeto)
        lista.GuardarXML(rol,nombre,apellido,telefono,correo,contrasena)
        return redirect('default')
    return render(request, 'principal/login.html')


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

import xml.dom.minidom as minidom

def cargarPeliculasDesdeXML():
    doc = minidom.parse('peliculas.xml')  # Parsear el archivo XML

    peliculas = []
    categorias = doc.getElementsByTagName('categoria')
    for categoria in categorias:
        nombre_categoria = categoria.getElementsByTagName('nombre')[0].firstChild.data
        peliculas_categoria = categoria.getElementsByTagName('pelicula')
        for pelicula in peliculas_categoria:
            titulo = pelicula.getElementsByTagName('titulo')[0].firstChild.data
            director = pelicula.getElementsByTagName('director')[0].firstChild.data
            anio = pelicula.getElementsByTagName('anio')[0].firstChild.data
            fecha = pelicula.getElementsByTagName('fecha')[0].firstChild.data
            hora = pelicula.getElementsByTagName('hora')[0].firstChild.data
            imagen = pelicula.getElementsByTagName('imagen')[0].firstChild.data
            precio = pelicula.getElementsByTagName('precio')[0].firstChild.data

            

            peliculas.append({
                'categoria': nombre_categoria,
                'titulo': titulo,
                'director': director,
                'anio': anio,
                'fecha': fecha,
                'hora': hora,
                'imagen': imagen,
                'precio': precio
            })



    return peliculas



#carga tabla de administrador
def listaPeli(request):
    peliculas = list(listaCir)
    return render(request, 'peliculas/listaPeliculas.html', {'peliculas': peliculas})

def cargaXML(request):
    if request.method == 'POST':
        listaCir.CargarPelis(pelis)

        response = requests.get('http://localhost:5007/getPeliculas')
        peliculas = response.json()

        for categoria in peliculas['categoria']:
             nombre_categoria = categoria['nombre']
             print("Categoría", nombre_categoria)

             peliculas = categoria['peliculas']['pelicula']
             for pelicula in peliculas:
                titulo = pelicula['titulo']
                director=pelicula['director']
                anio=pelicula['anio']
                fecha=pelicula['fecha']
                hora=pelicula['hora']
                imagen= pelicula['imagen']
                precio =pelicula['precio']
                objeto = Peliculas(nombre_categoria,titulo,director,anio,fecha,hora,imagen,precio)
                listaCir.add(objeto)
                
        
        return redirect('listaPeli')
    return render(request, 'peliculas/listaPeliculas.html', {'peliculas': listaCir})


def cancelaBoleto(request):
    historial = listaCir.historial 
    
    return render(request,'boletos/boletos.html',{'historial': historial})

def eliminaBoleto(request,posicion):
    historial = listaCir.historial 
    del historial[posicion]
    return redirect('cancelaBoleto')


#carga Tabla de cliente
def listaPeliCliente(request):
    peli = list(listaCir)
    
    return render(request, 'principal/cliente.html', {'peliculas': peli})


def cargalistaCliente(request):
    if request.method == 'POST':
        listaCir.mostrar_datos()
    return render(request ,'principal/cliente.html', {'peli': list(listaCir)})


def compraBoletoPost(request, nombre):
    listaCir.favs(nombre)
    if request.method == 'POST':
        numBoletos = request.POST.get('numBoletos')
        imagen = request.POST.get('imagen')
        salaElegida = request.POST.get('salaElegida')
        nit = request.POST.get('nit')
        direccion = request.POST.get('direccion')
        tipoPago = request.POST.get('formaPago')
        numero = request.POST.get('numero')
        titular = request.POST.get('titular')
        fecha=request.POST.get('fecha')
        listaCir.comprarBoletos(nombre,imagen, numBoletos, salaElegida, nit, direccion,tipoPago)
        if tipoPago != "efectivo":
            listTar.agregarTarjeta(tipoPago,numero,titular,fecha)
        salas_disponibles = listaCir.mostrarSalas()
        return render(request, 'principal/compraBoletos.html', {'boletos': listaCir, 'salas_disponibles': salas_disponibles})
    else:
        salas_disponibles = listaCir.mostrarSalas()
        return render(request, 'principal/compraBoletos.html', {'boletos': listaCir, 'salas_disponibles': salas_disponibles})
    


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
        
        listaCir.registraPeli(categoria, titulo, director, anio, fecha, hora, imagen, precio)
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

            # Llamar a la función editar para actualizar el archivo XML
            listaCir.editar(titulo, peli.categoria, peli.titulo, peli.director, peli.anio, peli.fecha, peli.hora, peli.imagen, peli.precio)
            
            return redirect('listaPeli')
        return render(request, 'peliculas/actualizarPeli.html', {'peli': peli})
    return redirect('listaPeli')

def eliminarPeli(request, titulo):   
    listaCir.eliminarPelicula(titulo)
    return redirect('listaPeli')

def cargaXMLSalas(request):
    if request.method == 'POST':
        listaDob.cargaSalas(salas)

        response = requests.get('http://localhost:5007/getSalas')
        salasAPI = response.json()

        for sala in salasAPI["cine"]["salas"]["sala"]:
            numero = sala["numero"]
            asientos = sala["asientos"]
            objeto = Salas(salasAPI["cine"]["nombre"], numero, asientos)
            listaDob.add(objeto)
            print(objeto.numero)
        return redirect('listaSalas')
    return render(request, 'salas/listaSalas.html', {'sala': listaDob})

def listaSalas(request):
    sala = list(listaDob)
    return render(request, 'salas/listaSalas.html', {'salas': sala})

def crearSala(request):
    if request.method == 'POST':
        cine = request.POST.get('cine')
        numero =request.POST.get('numero')
        asientos = request.POST.get('asientos')
        listaDob.AgregarNuevaSala(cine,numero,asientos)
        listaDob.agregarSala(cine,numero,asientos,salas)
        return redirect('listaSalas')
    return render(request, 'salas/crearSala.html')

def actualizarSalas(request, numero):
    sala = next((sala for sala in listaDob if sala.numero == numero), None)
    if sala:
        if request.method == 'POST':
            sala.cine = request.POST.get('cine')
            sala.numero = request.POST.get('numero')
            sala.asientos = request.POST.get('asientos')
            listaDob.editarSalas(numero, sala.numero, sala.asientos, salas)
            
            return redirect('listaSalas')
        return render(request, 'salas/actualizarSalas.html', {'sala': sala})

    return redirect('listaSalas')

def eliminarSalas(request, numero):
    listaDob.eliminarSalas(numero)
    return redirect('listaSalas')
    


def listaTarjeta(request):
    tarjeta = list(listTar)
    return render(request, 'tarjetas/listaTarjetas.html', {'tarjeta': tarjeta})

def cargaXMLTarjetas(request):
    if request.method == 'POST':
        listTar.cargarTarjetas()
        response = requests.get('http://localhost:5007/getTarjetas')
        salasAPI = response.json()

        for sala in salasAPI["tarjeta"]:
            tipo = sala["tipo"]
            numero = sala["numero"]
            titular = sala["titular"]
            fecha = sala["fecha_expiracion"]
            objeto = Tarjetas(tipo,numero,titular,fecha)
            listTar.add(objeto)
            



        return redirect('listaTarjeta')
    return render(request, 'tarjetas/listaTarjetas.html', {'tarjeta': listTar})

def listaTarjeta(request):
    tarjeta = list(listTar)
    return render(request, 'tarjetas/listaTarjetas.html', {'tarjeta': tarjeta})

def crearTarjeta(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        numero = request.POST.get('numero')
        titular = request.POST.get('titular')
        fecha = request.POST.get('fecha')
        listTar.agregarTarjeta(tipo, numero, titular, fecha)
        return redirect('listaTarjeta')
    return render(request, 'tarjetas/crearTarjeta.html')

def actualizarTarjeta(request, numero):
    tarjeta = next((tarjeta for tarjeta in listTar if tarjeta.numero == numero), None)
    if tarjeta:
        if request.method == 'POST':
            tarjeta.tipo = request.POST.get('tipp')
            tarjeta.numero = request.POST.get('numero')
            tarjeta.titular = request.POST.get('titular')
            tarjeta.fecha = request.POST.get('fecha')
            listTar.editarTarjeta(numero, tarjeta.tipo, tarjeta.numero , tarjeta.titular,tarjeta.fecha)
            
            return redirect('listaTarjeta')
        return render(request, 'tarjetas/actualizarTarjeta.html', {'tarjeta': tarjeta})

    return redirect('listaTarjeta')

def eliminarTarjeta(request, numero):
    listTar.eliminarTarjeta(numero)
    return redirect('listaTarjeta')
    

def historial(request):
    historial = listaCir.historial  
    return render(request, 'principal/historial.html', {'historial': historial})
        

