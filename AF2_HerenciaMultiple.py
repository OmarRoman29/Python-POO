class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola soy {self.nombre}"

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es {self.habilidad}"

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, habilidad, salario):
        Persona.__init__(self, nombre, edad)
        Artista.__init__(self, habilidad)
        self.salario = salario

    # Puedes llegar a redefinir métodos
    def presentarse(self):
        return f"Hola soy {self.nombre} y me dedico a {self.habilidad}"

    def cobrar(self):
        return f"{self.nombre} a cobrado {self.salario}"

empleado = EmpleadoArtista("Juan", 15, "Bailar", 15.2)

print(empleado.presentarse())
print(empleado.mostrar_habilidad())
print(empleado.cobrar())

# Verificar si es herencia
print(f"Empleado es subclase de artista?: {issubclass(EmpleadoArtista, Artista)}")
print(f"Persona es subclase de artista?: {issubclass(Persona, Artista)}")

roberto = Artista("Bailar")

# Verificar si es instancia de una clase
print(f"'empleado' es instancia de EmpleadoArtista?: {isinstance(empleado, EmpleadoArtista)}")
print(f"'empleado' es instancia de Persona?: {isinstance(empleado, Persona)}")
print(f"'roberto' es instancia de Persona?: {isinstance(roberto, Persona)}")
