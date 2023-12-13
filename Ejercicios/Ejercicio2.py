# Crear un sistema para una escuela. En este sistema, vamos a tener
# dos clases principales: Persona y Estudiante. La clase Persona
# tendrá los atributos de 'nombre' y 'edad' y un método que imprima
# el nombre y la edad de la peronsa. La clase Estudiante heredará de
# la clase Persona y también tendrá un atributo adicional 'grado' y
# tendrá un método que imprima el grado del estudiante

# Deberás utilizar super en el constructor para reutilizar el código
# de la clase padre (Persona). Luego crea una instanicia de la clase
# Estudiante e imprime sus atributos y utiliza sus métodos para 
# asegurarse de que todo funciona correctamente

class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def info_persona(self) -> str:
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado) -> None:
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self) -> str:
        return f"Grado: {self.grado}"

estudiante = Estudiante("Juan", 15, "3°")
print(estudiante.info_persona())
print(estudiante.mostrar_grado())
