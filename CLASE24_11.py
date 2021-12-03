"""
Para cada clase creada por proyecto(carpeta) se debe generar un fichero.py 

clase1: En un fichero
clase2: en otro fichero
si quiero utilizar la clase 1 dentro de la clase2:
import clase1
Como ambos estan dentro del proyecto se pueden importar y utilizar uno dentro
del otro


cada fichero con un concepto
pero un concepto en cada fichero

CONCEPTOS FUNDAMENTALES PARA LA PROGRAMACION ORIENTADA A OBJETOS:
    1. ENCAPSULACION:
        proviene de las funciones
        los metodos y atributos se corresponden con ciertas clases, no con 
        todas
    2. POLIMORFISMO:
        proviene de las funciones
        Capacidad que tiene el programador de utilizar una unica funcion con 
        multiples parametros
        ejemplo: range (a,b,c) dependiendo de la cantidad de variblaes que 
        recibe su comportamiento varía
        Un objeto puede actuar de muchas formas
        Podemos llegar al mismo resultado mediante el uso de diferentes 
        parametros
    3. HERENCIA:
        no proviene de las funciones, pertenece a los objetos
        ejemplo:
            figura 2D:
                comportamiento:
                    Area
                    Perimetro
            Dentro de las figuras 2D hacemos distincion:
                circulo:
                    atributo: 
                        radio
                    comportamiento:
                        area
                        perimetro
                poligono:
                    Atributo:
                        numero de lados
                        longitud
                    comportamiento:
                        area 
                        perimetro
                        
                si definimos al poligono y al cicrulo como clases-> figura 2D 
                es la superclase
                la derivada de un superclase se conoce como sub clase
En *1 la palabra pass se utiliza para omitir la definicion del area. Es 
necesario definir la funcion area
dentro del concepto figura para que se le atribuya a todo objeto perteneciente
a objeto
En *2 el concepto es ademas de tipo objeto, de tipo figura, es decir se 
concreta mas la clase
Para que exista el circulo tiene que estar definido previamente la figura


"""
#*1
class Figura(object):
    def Area():
        pass
        
#*2 
class Circulo(Figura):
    def __init__(self, radio):
        self.Radio= radio
#Area/ Perimetro del circulo es una propiedad del circulo      
    def Area(self):
        return 3.14*(self.Radio**2)
    
class Alumno():
    def __init__ (self, fechaNac):
        self.fechaNac = fechaNac
 #Esto no es una propiedad, es una funcion
#Propiedad: efecto cuya causa es interna       
    def Edad(self, fechaActual):
        dias= fechaActual-self.fechaNac
        return dias/365
class Cuadrado(Figura):
    def __init__ (self, lado):
        self.Lado = lado
    def Area(self):
        return self.Lado **2
    
"""
ejemplo de herencia:
Empleados (todos tienen x atributos -> se define 
el constructor)
    TIPOS DE EMPLEADOS: Distintas funciones y atributos en 
    cada uno
    Constructor
    Tecnicos
"""

class Empleado(object):
    def __init__ (self, salario):
        self.__salario = salario
    def RetirarNomina (self):
        self.__salario =0
    def getSalario(self):
        return self.__salario
class Tecnico (Empleado):
    def __init__ (self, puesto, salario):
        super().__init__(salario)
        self.Puesto = puesto
        
e = Empleado(5)
t= Tecnico ("Contabilidad", 5)
print (e.getSalario())

"""Atributos internos = atributos privados
"self.Salario= 45" es un atributo publico 
que se puede modificar
"self.__Salario=45" se tranforma en un atributo privado 
el cual no se puede modificar
el doble guion al principio hace que el atributo pase 
de publico a privado

"""    