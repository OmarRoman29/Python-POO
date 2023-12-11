
# Objetos, herencia y constructores

# Crear un Objeto llamado alumno cuya estructura tenga como atributos:
# Matrícula, Nombre, CURP, promedio, porcentaje Beca, Colonia, Calle,
# Número, CP y Ciudad. Capture datos desde el teclado para almacenarlos
# en cada uno de los atributos, si el promedio tecleado es igual a 10.0
# entonces asignarle un porcentaje de beca de 50%, si 10> promedio>=9.0
# asignarle un porcentaje de 30%, si 9.0> promedio>=8.0 asignarle un
# 20% de beca.

# Agregar otro objeto llamado profesor cuya estructura contenga los
# siguientes atributos: Clave del Profesor, Nombre, departamento 
# Académico,  Num horas, Num de asignaturas, Colonia, Calle, Número,
# CP y Ciudad. Capture datos desde el teclado para almacenarlos en
# cada uno de los miembros.

class Persona:
    def __init__(self, nombre, colonia, calle, cp, ciudad):
        self.nombre = nombre
        self.colonia = colonia
        self.calle = calle
        self.cp = cp
        self.ciudad = ciudad
    def imprimirPersona(self):
        print(f"""
              Nombre: {self.nombre}
              Colonia: {self.colonia}
              Calle: {self.calle}
              CP: {self.cp}
              Ciudad: {self.ciudad}
              """)

class Estudiante(Persona):
    def __init__(self, nombre, colonia, calle, cp, ciudad, matricula, promedio):
        super().__init__(nombre, colonia, calle, cp, ciudad)
        self.matricula = matricula
        self.promedio = float(promedio)
        self.porcBeca = self.calcBeca()
    
    def calcBeca(self):
        if(self.promedio == 10.0):
            return 50
        elif(self.promedio<10.0 and self.promedio>=9.0):
            return 30
        elif(self.promedio<9.0 and self.promedio>=8.0):
            return 20
        else:
            return 0

    def imprimirEstudiante(self):
        print(f"""
              Matricula: {self.matricula}
              Promedio: {self.promedio}
              Porcentaje Beca: {self.porcBeca}
              """)

class Profesor(Persona):
    def __init__(self, nombre, colonia, calle, cp, ciudad, clave, departamento, numH, numA):
        super().__init__(nombre, colonia, calle, cp, ciudad)
        self.clave = clave
        self.departamento = departamento
        self.numH = numH
        self.numA = numA

    def imprimirProfesor(self):
        print(f"""
              Clave: {self.clave}
              Departamento: {self.departamento}
              Num Horas: {self.numH}
              Num Asignaturas: {self.numA}
              """)

print("Datos del estudiante: ")
nombre = input("Ingresa el nombre: ")
colonia = input("Ingresa la colonia: ")
calle = input("Ingresa la calle: ")
cp = input("Ingresa el codigo postal: ")
ciudad = input("Ingresa la ciudad: ")
matricula = input("Ingresa la matrícula: ")
promedio = input("Ingresa el promedio: ")

estudiante = Estudiante(nombre, colonia, calle, cp, ciudad, matricula, promedio)
estudiante.imprimirPersona()
estudiante.imprimirEstudiante()

print("Datos del profesor: ")
nombre = input("Ingresa el nombre: ")
colonia = input("Ingresa la colonia: ")
calle = input("Ingresa la calle: ")
cp = input("Ingresa el codigo postal: ")
ciudad = input("Ingresa la ciudad: ")
clave = input("Ingresa la clave: ")
departamento = input("Ingresa el departamento: ")
numH = input("Ingresa el num de horas: ")
numA = input("Ingresa el num de asignaturas: ")

profesor = Profesor(nombre, colonia, calle, cp, ciudad, clave, departamento, numH, numA)
profesor.imprimirPersona()
profesor.imprimirProfesor()
