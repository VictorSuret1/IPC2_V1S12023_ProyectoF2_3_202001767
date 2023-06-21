import xml.etree.ElementTree as ET
from proyecto.fase1.nodos import NodoCircular
from proyecto.fase1.cons import Peliculas

class listaDobleCircular:
    def __init__(self):
        self.cabeza = None
        self.lista = []
        self.historial = []
        self.numero_boleto = 1

    def add(self, dato):
        nuevo_nodo = NodoCircular(dato)

        if self.cabeza is None:
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            ultimo = self.cabeza.anterior

            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = ultimo

            self.cabeza.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo

    def CargarPelis(self,ruta):
        tree = ET.parse(ruta)
        root = tree.getroot()
        for categoria in root.findall("categoria"):
            nombre = categoria.find('nombre').text
           
            pelicula = categoria.find('peliculas')

            for peli in pelicula.findall('pelicula'):
                titulo = peli.find('titulo').text
                director = peli.find('director').text
                anio = peli.find('anio').text
                fecha = peli.find('fecha').text
                hora= peli.find('hora').text
                imagen = peli.find('imagen').text
                precio= peli.find('precio').text
                peli = Peliculas(nombre,titulo,director,anio,fecha,hora,imagen,precio)
                self.add(peli)

    def loop(self):
        if self.cabeza is not None:
            actual = self.cabeza
            while True:
                yield actual.dato
                actual = actual.siguiente
                if actual == self.cabeza:
                    break

    def __iter__(self):
     return iter(self.loop())

    def MostrarLista(self):
        actual = self.cabeza

        if actual is None:
            print("La lista está vacía.")
            return

        print("Datos en la lista:")
        while True:
            print(f"Titulo: {actual.dato.titulo} | Director: {actual.dato.director} | Anio: {actual.dato.anio} | Fecha: {actual.dato.fecha} | Hora: {actual.dato.hora}")

            actual = actual.siguiente
            if actual == self.cabeza:
                # Se ha recorrido toda la lista
                break


    

    def registraPeli(self):
        categoria = input("Ingresa la Categoria : ")
        titulo = input("Ingresa el Titulo : ")
        director = input("Ingresa el director : ")
        anio = input("Ingresa el anio : ")
        fecha = input("Ingresa el fecha : ")
        hora = input("Ingresa el hora : ")

        peli = Peliculas(categoria, titulo, director, anio, fecha, hora)
        self.add(peli)
        # Agregar los datos al archivo XML
        tree = ET.parse('peliculas.xml')
        root = tree.getroot()

        # Encontrar la categoría existente o crear una nueva
        categorias = root.findall('categoria')
        categoria_existente = False
        for cat in categorias:
            if cat.find('nombre').text.lower() == categoria.lower():
                categoria_existente = True
                peliculas = cat.find('peliculas')
                nueva_pelicula = ET.SubElement(peliculas, 'pelicula')
                ET.SubElement(nueva_pelicula, 'titulo').text = titulo
                ET.SubElement(nueva_pelicula, 'director').text = director
                ET.SubElement(nueva_pelicula, 'anio').text = anio
                ET.SubElement(nueva_pelicula, 'fecha').text = fecha
                ET.SubElement(nueva_pelicula, 'hora').text = hora
                break

        # Si la categoría no existe, crear una nueva
        if not categoria_existente:
            nueva_categoria = ET.SubElement(root, 'categoria')
            ET.SubElement(nueva_categoria, 'nombre').text = categoria
            peliculas = ET.SubElement(nueva_categoria, 'peliculas')
            nueva_pelicula = ET.SubElement(peliculas, 'pelicula')
            ET.SubElement(nueva_pelicula, 'titulo').text = titulo
            ET.SubElement(nueva_pelicula, 'director').text = director
            ET.SubElement(nueva_pelicula, 'anio').text = anio
            ET.SubElement(nueva_pelicula, 'fecha').text = fecha
            ET.SubElement(nueva_pelicula, 'hora').text = hora

        # Guardar los cambios en el archivo XML
        tree.write('peliculas.xml')

   
    def EditarPelicula(self, titulo):
        actual = self.cabeza

        # Buscar la película por título exacto
        while actual is not None:
            if actual.dato.titulo == titulo:
                print("Presione Enter para dejar el dato actual.")
                nuevoTitulo = input(f"Ingrese el nuevo título: actual: {actual.dato.titulo} nuevo: ") or actual.dato.titulo
                nuevoDirector = input(f"Ingrese el nuevo director: actual: {actual.dato.director} nuevo: ") or actual.dato.director
                nuevoAnio = input(f"Ingrese el nuevo año: actual: {actual.dato.anio} nuevo: ") or actual.dato.anio
                nuevaFecha = input(f"Ingrese la nueva fecha: actual: {actual.dato.fecha} nuevo: ") or actual.dato.fecha
                nuevaHora = input(f"Ingrese la nueva hora: actual: {actual.dato.hora} nuevo: ") or actual.dato.hora

                break
            actual = actual.siguiente
            

        # Si se encontró la película
        if actual is not None:
            
            # Actualizar los datos de la película en la lista doble circular
            actual.dato.titulo = nuevoTitulo
            actual.dato.director = nuevoDirector
            actual.dato.anio = nuevoAnio
            actual.dato.fecha = nuevaFecha
            actual.dato.hora = nuevaHora

            # Actualizar los datos en el archivo XML
            tree = ET.parse("peliculas.xml")
            root = tree.getroot()

            for categoria in root.findall("categoria"):
                peliculas = categoria.find("peliculas")
                for peli in peliculas.findall("pelicula"):
                    titulo_actual = peli.find("titulo").text
                    if titulo_actual == titulo:
                        peli.find("titulo").text = nuevoTitulo
                        peli.find("director").text = nuevoDirector
                        peli.find("anio").text = nuevoAnio
                        peli.find("fecha").text = nuevaFecha
                        peli.find("hora").text = nuevaHora
                        break

            tree.write("peliculas.xml")
            print("Película editada exitosamente.")
        else:
            print("Película no encontrada.")

    def eliminarPelicula(self, titulo):
        nodo_actual = self.cabeza

        if nodo_actual is None:
            print("La lista está vacía.")
            return

        # Buscar el nodo que contiene la película con el título dado
        while True:
            if nodo_actual.dato.titulo == titulo:
                # Eliminar la película de la lista
                if nodo_actual.siguiente == nodo_actual:  # Único nodo en la lista
                    self.cabeza = None
                else:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente.anterior = nodo_actual.anterior

                    if nodo_actual == self.cabeza:  # Si se eliminó el nodo cabeza
                        self.cabeza = nodo_actual.siguiente

                break

            nodo_actual = nodo_actual.siguiente

            # Se completó una vuelta completa en la lista, la película no se encontró
            if nodo_actual == self.cabeza:
                print("La película no se encontró en la lista.")
                return

        # Eliminar la película del archivo XML
        tree = ET.parse('peliculas.xml')
        root = tree.getroot()

        for categoria in root.findall("categoria"):
            peliculas = categoria.find('peliculas')

            for pelicula in peliculas.findall('pelicula'):
                if pelicula.find('titulo').text == titulo:
                    peliculas.remove(pelicula)

                    # Eliminar la categoría si no tiene más películas
                    if len(peliculas.findall('pelicula')) == 0:
                        root.remove(categoria)

                    break

        # Guardar los cambios en el archivo XML
        tree.write('peliculas.xml')

        print("La película se eliminó correctamente de la lista y el archivo XML.")

    def mostrarPorCategoria(self, categoria):
        actual = self.cabeza

        if actual is None:
            print("La lista está vacía.")
            return

        while True:
            if actual.dato.categoria == categoria:
                print(f"Categoría: {actual.dato.categoria} Titulo: {actual.dato.titulo} Director: {actual.dato.director} Año: {actual.dato.anio} Fecha: {actual.dato.fecha} Hora: {actual.dato.hora}")
                

            actual = actual.siguiente

            if actual == self.cabeza:
                break

    def mostrarGeneral(self):
        actual = self.cabeza

        if actual is None:
            print("La lista está vacía.")
            return

        print("Datos en la lista:")
        while True:
            print(f"Titulo: {actual.dato.titulo} | Director: {actual.dato.director} | Anio: {actual.dato.anio} | Fecha: {actual.dato.fecha} | Hora: {actual.dato.hora}")

            actual = actual.siguiente
            if actual == self.cabeza:
                # Se ha recorrido toda la lista
                break
    
    def mostrarCategorias(self):
        actual = self.cabeza

        if actual is None:
            print("La lista está vacía.")
            return

        categorias = set()

        while True:
            categorias.add(actual.dato.categoria)
            actual = actual.siguiente

            if actual == self.cabeza:
                break

        print("Categorías disponibles:")
        i=0
        for categoria in categorias:
            print(categoria)
            

    def marcarComoFavorita(self, titulo):
        actual = self.cabeza

        if actual is None:
            print("La lista está vacía.")
            return

        while True:
            if actual.dato.titulo == titulo:
                actual.dato.favorita = True
                print(f"La película '{titulo}' ha sido marcada como favorita.")
                return

            actual = actual.siguiente

            if actual == self.cabeza:
                break

        print(f"No se encontró la película '{titulo}' en la lista.")


    def favs(self,nombrePeli):
        actual = self.cabeza

        if actual is None:
            print("La lista original está vacía.")
            return self.lista
        
        while True:
            pelicula = actual.dato
            if pelicula.titulo == nombrePeli:
                if pelicula not in self.lista:
                    self.lista.append(pelicula)
                

            actual = actual.siguiente

            if actual == self.cabeza:
                break
        
        return self.lista
    
    def mostraNuevo(self,nueva_lista):
        if len(nueva_lista) > 0:
            print("Datos de Peliculas Favoritas:")
            for pelicula in nueva_lista:
                print(f"Título: {pelicula.titulo} | Director: {pelicula.director} | Año: {pelicula.anio} | Fecha: {pelicula.fecha} | Hora: {pelicula.hora}")
        else:
            print("No hay datos de Peliculas Favoritas")

    def comprarBoletos(self, nombrePeli):

        peliculas = self.favs(nombrePeli)

        if not peliculas:
            print("No se encontró la película en la lista.")
            return

        pelicula = peliculas[0]

        numBoletos = int(input("Ingrese el número de boletos que desea comprar: "))

        while True:
            print("Salas disponibles:")
            salas_disponibles = self.mostrarSalas()

            salaElegida = input("Seleccione una sala: ")

            if salaElegida not in salas_disponibles:
                print("La sala seleccionada no es válida.")
                continue

            asientos_sala = salas_disponibles[salaElegida]

            if numBoletos > asientos_sala:
                print("No hay suficientes asientos en la sala seleccionada.")
                break

            monto_total = numBoletos * 42

            print(f"Monto total: {monto_total}")

            nit = input("Ingrese el NIT o ingrese 'CF' para terminar: ")
            if nit== "CF":
                direccion = "CF"
            else:
                direccion = input("Ingrese la dirección de facturación: ")

            

            # Crear un diccionario con los detalles de la compra
            detalleDeCompra = {
                "Pelicula": pelicula.titulo,
                "Fecha": pelicula.fecha,
                "Hora": pelicula.hora,
                "Num. boletos": numBoletos,
                "Num. asiento": salaElegida,
                "Monto pago": monto_total,
                "NIT": nit,
                "Dirección": direccion
            }

            # Agregar el detalle de la compra al historial
            self.historial.append(detalleDeCompra)

            print("Boleto comprado exitosamente.")
            break
    
    def generarNumeroBoleto(self):
        numero_boleto = f"#USACIPC2_202001767_{self.numBoletos}"
        self.numero_boleto += 1
        return numero_boleto

    def mostrarHistorial(self):
        
        for compra in self.historial:
            print("Detalles de la compra:")
            print(f"Película: {compra['Pelicula']}")
            print(f"Fecha: {compra['Fecha']}")
            print(f"Hora: {compra['Hora']}")
            print(f"Número de boletos: {compra['Num. boletos']}")
            print(f"Número de asiento: {compra['Num. asiento']}")
            print(f"Monto pagado: {compra['Monto pago']}")
            print(f"NIT: {compra['NIT']}")
            print(f"Dirección: {compra['Dirección']}")
            print("----------------------------")
    
    def mostrarSalas(self):
        tree = ET.parse('salas.xml')
        root = tree.getroot()
        
        salas_disponibles = {}
        
        for cine in root.findall("cine"):
            nombre_cine = cine.find('nombre').text
            
            for sala in cine.findall('salas/sala'):
                numero_sala = sala.find('numero').text
                asientos = int(sala.find('asientos').text)
                salas_disponibles[numero_sala] = asientos
            
        for sala, asientos in salas_disponibles.items():
            print(f"Sala: {sala} | Asientos disponibles: {asientos}")
        
        return salas_disponibles