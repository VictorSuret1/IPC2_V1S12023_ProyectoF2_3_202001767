from proyecto.fase1.nodos import NodoDobleTarjeta

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
    
    