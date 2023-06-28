from proyecto.fase1.nodos import NodoDobleTarjeta
from proyecto.fase1.cons import Tarjetas
import xml.etree.ElementTree as ET

class listaDobleTarjeta:
    def __init__(self):
        self.cabeza = None


    def add(self, dato):
        nuevo_nodo = NodoDobleTarjeta(dato)

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
    
    def agregarTarjeta(self, tipo, numero, titular, fecha):
        # Cargar el archivo XML existente
        archivo_xml = "tarjetas.xml"
        try:
            arbol_xml = ET.parse(archivo_xml)
            tarjetas_elemento = arbol_xml.getroot()
        except FileNotFoundError:
            # Si el archivo no existe, crear uno nuevo
            tarjetas_elemento = ET.Element("tarjetas")
            arbol_xml = ET.ElementTree(tarjetas_elemento)

        # Crear un elemento para la nueva tarjeta y agregar sus subelementos
        tarjeta_elemento = ET.SubElement(tarjetas_elemento, "tarjeta")
        tipo_elemento = ET.SubElement(tarjeta_elemento, "tipo")
        tipo_elemento.text = tipo
        numero_elemento = ET.SubElement(tarjeta_elemento, "numero")
        numero_elemento.text = numero
        titular_elemento = ET.SubElement(tarjeta_elemento, "titular")
        titular_elemento.text = titular
        fecha_elemento = ET.SubElement(tarjeta_elemento, "fecha_expiracion")
        fecha_elemento.text = fecha

        # Guardar el árbol XML en el archivo
        arbol_xml.write(archivo_xml)

    def cargarTarjetas(self):
        tree = ET.parse("tarjetas.xml")
        root = tree.getroot()

        for tarjeta in root.findall('tarjeta'):
            tipo = tarjeta.find('tipo').text
            numero = tarjeta.find('numero').text
            titular = tarjeta.find('titular').text
            fecha = tarjeta.find('fecha_expiracion').text

            objeto = Tarjetas(tipo, numero, titular, fecha)
            self.add(objeto)


    def editarTarjeta(self,numero, nuevoTipo,nuevoNumero,nuevoTitular,nuevaFecha):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.numero == numero:
                actual.dato.numero = nuevoNumero
                actual.dato.titular = nuevoTitular
                actual.dato.fecha = nuevaFecha

                tree = ET.parse("tarjetas.xml")
                root = tree.getroot()

                for usuario in root.findall('tarjeta'):
                    tarjetaActual = usuario.find('numero').text
                    if tarjetaActual == numero:
                        usuario.find('tipo').text = nuevoTipo
                        usuario.find('numero').text = nuevoNumero
                        usuario.find('titular').text = nuevoTitular
                        usuario.find('fecha').text = nuevaFecha

                        tree.write("tarjetas.xml")
                        print("Usuario editado exitosamente.")
                break

            actual = actual.siguiente

        if actual is None:
            print("Usuario no encontrado.")


    def eliminarTarjeta(self, numero):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.numero == numero:
                # Eliminar el nodo de la lista
                if actual.anterior is None:
                    self.cabeza = actual.siguiente
                    if self.cabeza is not None:
                        self.cabeza.anterior = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente is not None:
                        actual.siguiente.anterior = actual.anterior

                # Eliminar el nodo del archivo XML
                tree = ET.parse("tarjetas.xml")
                root = tree.getroot()

                for tarjeta in root.findall('tarjeta'):
                    tarjeta_actual = tarjeta.find('numero').text
                    if tarjeta_actual == numero:
                        root.remove(tarjeta)
                        tree.write("tarjetas.xml")
                        print("Tarjeta eliminada exitosamente.")
                break

            actual = actual.siguiente

        if actual is None:
            print("Tarjeta no encontrada.")