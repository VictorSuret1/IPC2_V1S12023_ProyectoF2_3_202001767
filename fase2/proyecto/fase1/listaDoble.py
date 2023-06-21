from proyecto.fase1.nodos import NodoDoble
import xml.etree.ElementTree as ET
from proyecto.fase1.cons import Salas

class listaDoble:
    def __init__(self):
        self.cabeza = None


    def add(self, dato):
        nuevo_nodo = NodoDoble(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def cargaSalas(self,ruta):
        tree = ET.parse(ruta)
        root = tree.getroot()

        for categoria in root.findall("cine"):
            nombre = categoria.find('nombre').text
            sala = categoria.find('salas')

            for sal in sala.findall('sala'):
                numero = sal.find('numero').text
                asientos = sal.find('asientos').text
                sal = Salas(nombre,numero,asientos)
                self.add(sal)

    def mostrarDatos(self):
        actual = self.cabeza

        while actual is not None:
            sala = actual.dato
            print(f"Cine: {sala.cine} | Numero de Sala: {sala.numero} | Asientos: {sala.asientos}")
            actual = actual.siguiente

    def loop(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

    def __iter__(self):
        return iter(self.loop())

    def editarSalas(self):
        numSala = input("Ingrese el numero de sala que desea editar: ")
        actual = self.cabeza

        while actual is not None:
            if actual.dato.numero == numSala:
                print("Presione Enter para dejar el dato actual.")
                nuevoNum = input(f"Ingrese el nuevo número de sala: actual: {actual.dato.numero} nuevo: ") or actual.dato.numero
                nuevoAsientos = input(f"Ingrese el nuevo número de asientos: actual: {actual.dato.asientos} nuevo: ") or actual.dato.asientoss

                actual.dato.numero = nuevoNum
                actual.dato.asientos = nuevoAsientos

                # Actualizar el archivo XML
                tree = ET.parse('salas.xml')
                root = tree.getroot()

                for cine in root.findall("cine"):
                    for sala in cine.find('salas').findall('sala'):
                        if sala.find('numero').text == numSala:
                            sala.find('numero').text = nuevoNum
                            sala.find('asientos').text = nuevoAsientos

                tree.write('salas.xml')
                print("Los datos se han actualizado correctamente.")
                return

            actual = actual.siguiente

        print("El numero de sala ingresado no existe en la lista")


    def eliminarSalas(self):
        numero_sala = input("Ingrese el número de sala que desea eliminar: ")
        actual = self.cabeza

        while actual is not None:
            if actual.dato.numero == numero_sala:
                if actual.anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    actual.anterior.siguiente = actual.siguiente

                    if actual.siguiente is not None:
                        actual.siguiente.anterior = actual.anterior

                # Eliminar el nodo del archivo XML
                tree = ET.parse('salas.xml')
                root = tree.getroot()

                for cine in root.findall("cine"):
                    for sala in cine.find('salas').findall('sala'):
                        if sala.find('numero').text == numero_sala:
                            cine.find('salas').remove(sala)

                tree.write('salas.xml')
                print("La sala se ha eliminado correctamente.")
                return

            actual = actual.siguiente

        print("El número de sala ingresado no existe en la lista.")

    