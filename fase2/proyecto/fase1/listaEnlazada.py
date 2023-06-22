from proyecto.fase1.nodos import Nodo
import xml.etree.ElementTree as ET
from proyecto.fase1.cons import Usuario

class ListaEnlazada:  
    def __init__(self):
        self.cabeza = None

    def add(self, dato):
        
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def delete(self, correo):
        actual = self.head
        anterior = None

        while actual is not None:
            if actual.dato.correo == correo:
                if anterior is None:
                    self.head = actual.siguiente
                    return 1
                else:
                    anterior.siguiente = actual.siguiente
                    return 1
            anterior = actual
            actual = actual.siguiente


    def CargarXML(self, operacion,ruta):
        tree = ET.parse(ruta)
        root = tree.getroot()

        for indice, usuarios in enumerate(root.findall('usuario')):
            rol = usuarios.find('rol').text
            nombre = usuarios.find('nombre').text
            apellido = usuarios.find('apellido').text
            telefono = usuarios.find('telefono').text
            correo = usuarios.find('correo').text
            contra = usuarios.find('contrasena').text

            objeto = Usuario(rol,nombre,apellido,telefono,correo,contra)
            
            if operacion == 1 : # agregar datos a lista
                self.add(objeto)
            elif operacion == 2:
                correoEdit = input("ingresa el correo a editar: ")
                self.EditarUsuario(correoEdit)
                break

    
            
    def mostrarUsuarios(self):
    
        actual = self.cabeza

        while actual is not None:
            usuario = actual.dato
            print(f"rol: {usuario.rol} | nombre: {usuario.nombre} | apellido: {usuario.apellido} | telefono: {usuario.telefono} | correo: {usuario.correo} | contrasena: {usuario.contrasena}")
            actual = actual.siguiente            
            

    def EditarUsuario(self, correo, nuevoRol, nuevoNombre, nuevoApellido, nuevoTelefono, nuevoCorreo, nuevoContra):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.correo == correo:
                actual.dato.rol = nuevoRol
                actual.dato.nombre = nuevoNombre
                actual.dato.apellido = nuevoApellido
                actual.dato.telefono = nuevoTelefono
                actual.dato.correo = nuevoCorreo
                actual.dato.contrasena = nuevoContra

                tree = ET.parse("datos.xml")
                root = tree.getroot()

                for usuario in root.findall('usuario'):
                    correoActual = usuario.find('correo').text
                    if correoActual == correo:
                        usuario.find('rol').text = nuevoRol
                        usuario.find('nombre').text = nuevoNombre
                        usuario.find('apellido').text = nuevoApellido
                        usuario.find('telefono').text = nuevoTelefono
                        usuario.find('correo').text = nuevoCorreo
                        usuario.find('contrasena').text = nuevoContra
                        tree.write("datos.xml")
                        print("Usuario editado exitosamente.")
                break

            actual = actual.siguiente

        if actual is None:
            print("Usuario no encontrado.")
            
    def EliminarUsuario(self, correo):
        actual = self.cabeza
        previo = None

        # Buscar el usuario a eliminar
        while actual is not None:
            if actual.dato.correo == correo:
                break
            previo = actual
            actual = actual.siguiente

        # Si se encontró el usuario
        if actual is not None:
            # Eliminar el usuario de la lista enlazada
            if previo is None:
                self.cabeza = actual.siguiente
            else:
                previo.siguiente = actual.siguiente

            # Eliminar el usuario del archivo XML
            tree = ET.parse("datos.xml")
            root = tree.getroot()

            for usuario in root.findall('usuario'):
                if usuario.find('correo').text == correo:
                    root.remove(usuario)
                    tree.write("datos.xml")
                    break

            print("Usuario eliminado exitosamente.")
        else:
            print("Usuario no encontrado.")

    def GuardarXML(self,registro, nombre, apellido, telefono,correo,contrasena):
        nuevoUsuario = ET.Element('usuario')
        rol = ET.SubElement(nuevoUsuario, 'rol')
        rol.text = registro
        nombreE = ET.SubElement(nuevoUsuario, 'nombre')
        nombreE.text = nombre
        apellidoE = ET.SubElement(nuevoUsuario, 'apellido')
        apellidoE.text = apellido
        tel = ET.SubElement(nuevoUsuario, 'telefono')
        tel.text = telefono
        correoE = ET.SubElement(nuevoUsuario, 'correo')
        correoE.text = correo
        contra = ET.SubElement(nuevoUsuario, 'contrasena')
        contra.text = contrasena

        
        tree = ET.parse('datos.xml')# Cargar el xml
        root = tree.getroot()

        root.append(nuevoUsuario)

        tree.write('datos.xml')

    def Imprimir(self):
        actual = self.cabeza
        actual.dato.imprimir()
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir()

    def loop(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente
        

    def __iter__(self):
        return iter(self.loop())    

    def login(self, correo, contrasena):
        actual = self.cabeza
        rolUser = None
        
        while actual is not None:
            if actual.dato.correo == correo and actual.dato.contrasena == contrasena:
                if actual.dato.rol == "cliente":
                    print("Inicio de sesión exitoso como cliente.")
                    rolUser = "cliente"
                elif actual.dato.rol == "administrador":
                    print("Inicio de sesión exitoso como administrador.")
                    rolUser = "administrador"
                else:
                    print("No se pudo determinar el rol para el usuario.")
                break
            actual = actual.siguiente

        if rolUser is None:
            print("Inicio de sesión fallido. Credenciales incorrectas.")
        
        return rolUser
        