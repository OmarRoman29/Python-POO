# ¿Qué pasa si dos clases tienen el mismo atributo? 
# Para eso se tiene el Método de Resolución de Orden
# Si dos clases tienen el mismo método o atributo
# cuando se llame de ¿qué clase la va a tomar?

# MRO es el orden en el que python busca métodos y
# atributos en las clases. Cuando se llama super()
# entra en juego el MRO

class A:
    #pass
    def saludar(self):
        print("Hola desde A")

class B(A):
    pass
    #def saludar(self):
        #print("Hola desde B")

class C(A):
    pass
    #def saludar(self):
        #print("Hola desde C")

class D(B, C):
    pass
    #def saludar(self):
        #print("Hola desde D")

d = D()
#Siempre se da prioridad desde la clase que estemos llamando
print("Saludo desde D")
d.saludar()

#Busca algo así:
# Llama de la clase más a su izquierda, pero en el caso de
# B y C, elije según cuál hereda primero (Cuál se menciona 
# primero al momento de hacer la herencia)
#   >B
#  /  \
# A    >D
#  \  /
#   >C

class E:
    def saludar(self):
        print("saludo desde E")

class F(E):
    pass
    #def saludar(self):
        #print("saludo desde F")

class G(B,F):
    pass
    #def saludar(self):
        #print("Saludo desde G")

g = G()
g.saludar()

# En este caso va a buscar igual del elemento más a la izquierda
# pero en este caso antes de empezar a buscar por F debe terminar
# de buscar antes por el camino de B

# A -> B
#       \
#        > G
#       /
# E -> F

#Si quiero de g llamar a hablar de la clase E?
if (isinstance(g,E)):
    E.saludar(g)
