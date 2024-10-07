"""
Herencia: jerarquía entre clases. La subclase puede heredar de la clase padre 
(propiedades y métodos)
Ventaja: reutilización de código
"""

# HERENCIA
# Superclase

class Animal:
    
    # inicializador que recibe el parámetro name
    def __init__(self, name: str):
        self.name = name

    def sound(self): # las clases que heredan de Animal pueden sobrescribir este método para hacer un sonido específico
        pass


"""Subclases: heredan de la clase Animal al poner (Animal). 
El inicializador no lo ponemos en las clases
Dog y Cat porque es un nombre común que lo heredan de Animal. 
En el caso de la función sound, sí se redefinen en las clases Dog y Cat
En resumen: en este ejemplo, el inicializador es común pero la función sound se redefine
"""
        
# Clases que heredan de Animal(tienen las propiedades y métodos de Animal)    
# pueden tener sus propios métodos o sobrescribir los existentes   
class Dog(Animal):
    def sound(self): # sobrescribe el método sound de Animal
        print("Guau")

class Cat(Animal):
    def sound(self): # sobrescribe el método sound de Animal
        print("Miau")

my_animal = Animal("Animal")
my_animal.sound() # no hace nada
my_dog = Dog("Perro")
my_dog.sound()
my_cat = Cat("Gato")
my_cat.sound()


# POLIMORFISMO: capacidad de un objeto de tomar varias formas. 

""" En el caso anterior ya hay polimorfismo: si es un gato suena de una manera y si es
un perro, suena de otra. Es polimorfismo en tiempo de compilación
En este caso, vamos a definir la función print_sound()
Esto es polimorfismo en tiempo de ejecución 
"""

class Animal:

    def __init__(self, name):
        self.name = name

    def sound(self):
        pass      
        
class Dog(Animal):
    def sound(self):
        print("Guau")

class Cat(Animal):
    def sound(self):
        print("Miau")

# función que recibe un parámetro animal (instancia de la clase Animal o de una subclase)
def print_sound(animal: Animal):
    animal.sound() 
#la línea anterior llama al método sound del objeto animal que se pasa como parámetro
#animal puede ser una instancia de Dog, Cat o Animal; con lo cual se ejecutará el método correspondiente

my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Dog("Perro")
print_sound(my_dog)
my_cat = Cat("Gato")
print_sound(my_cat)

""""
RESUMEN:
Herencia: Dog y Cat heredan de Animal; ambas clases tienen acceso a los métodos y atributos de Animal
Sobrescritura de métodos: las clases Dog y Cat sobrescriben el método sound() para tener su propio comportamiento
Polimorfismo: a la función print_sound() se le pueden pasar diferentes tipos de animales y la función
invocará al método sound() correspondiente según la clase del objeto que se le pase (Dog, Cat...)
"""



