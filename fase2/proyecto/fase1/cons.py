class Usuario:
    def __init__(self,  rol, nombre, apellido, telefono, correo , contrasena):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
    
    def to_dict(self):
        return{
            'rol':self.rol,
            'nombre':self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'correo':self.correo,
            'contrasena':self.contrasena
        }
    
    def imprimir(self):
        print(f"rol: {self.rol} Nombre: {self.nombre} apellido: {self.apellido} telefono: {self.telefono} correo: {self.correo} contrasena: {self.contrasena}")


class Peliculas:
    def __init__(self, categoria, titulo, director, anio, fecha, hora,imagen,precio ):
        self.categoria = categoria
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora
        self.imagen = imagen
        self.precio = precio

    def to_dict(self):
        return {
            'categoria': self.categoria,
            'titulo': self.titulo,
            'director': self.director,
            'anio': self.anio,
            'fecha': self.fecha,
            'hora': self.hora,
            'imagen': self.imagen,
            'precio': self.precio
        }

class Salas:
    def __init__(self, cine, numero, asientos):
        self.cine = cine
        self.numero =numero
        self.asientos = asientos

    def to_dict(self):
        return{
            'cine': self.cine,
            'numero':self.numero,
            'asiientos':self.asientos
        }