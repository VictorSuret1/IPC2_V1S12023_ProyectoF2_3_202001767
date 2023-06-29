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

    def loop(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

    def __iter__(self):
        return iter(self.loop())

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

    def AgregarNuevaSala(self, cine, numero, asientos):
        nueva_sala = Salas(cine, numero, asientos)
        self.add(nueva_sala)

    def agregarSala(self, cine, numero, asientos, ruta):
        # Obtener el elemento raíz del archivo XML
        tree = ET.parse(ruta)
        root = tree.getroot()

        # Buscar el cine correspondiente o crearlo si no existe
        cine_elemento = None
        for cine_actual in root.findall("cine"):
            nombre = cine_actual.find('nombre').text
            if nombre == cine:
                cine_elemento = cine_actual
                break

        if cine_elemento is None:
            # Crear un nuevo elemento 'cine' y agregarlo al elemento raíz
            cine_elemento = ET.Element('cine')
            nombre_elemento = ET.SubElement(cine_elemento, 'nombre')
            nombre_elemento.text = cine
            salas_elemento = ET.SubElement(cine_elemento, 'salas')
            root.append(cine_elemento)
        else:
            salas_elemento = cine_elemento.find('salas')

        # Crear un nuevo elemento 'sala' y agregarlo a las salas del cine
        nueva_sala = ET.Element('sala')
        numero_elemento = ET.SubElement(nueva_sala, 'numero')
        numero_elemento.text = numero
        asientos_elemento = ET.SubElement(nueva_sala, 'asientos')
        asientos_elemento.text = asientos
        salas_elemento.append(nueva_sala)

        # Guardar los cambios en el archivo XML
        tree.write(ruta)
        print("Sala agregada correctamente.")


    def mostrarDatos(self):
        actual = self.cabeza

        while actual is not None:
            sala = actual.dato
            print(f"Cine: {sala.cine} | Numero de Sala: {sala.numero} | Asientos: {sala.asientos}")
            actual = actual.siguiente

 

    def editarSalas(self, numSala, nuevoNum, nuevoAsientos, ruta):
        actual = self.cabeza
        sala_encontrada = False

        while actual is not None:
            if actual.dato.numero == numSala:
                actual.dato.numero = nuevoNum
                actual.dato.asientos = nuevoAsientos
                sala_encontrada = True
                break

            actual = actual.siguiente

        if sala_encontrada:
            tree = ET.parse(ruta)
            root = tree.getroot()

            for cine in root.findall("cine"):
                for sala in cine.find('salas').findall('sala'):
                    if sala.find('numero').text == numSala:
                        sala.find('numero').text = nuevoNum
                        sala.find('asientos').text = nuevoAsientos

            tree.write(ruta)
            print("Sala actualizada correctamente.")
        else:
            print("El número de sala ingresado no existe en la lista.")

    def eliminarSalas(self,numero_sala):
        
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

    