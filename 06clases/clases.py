"""
Los objetos son entidades con unas características. Existen algunos propios del lenguaje
pero ahora vamos a ver cómo crear objetos que no existen en el lenguaje

En Python, cuando trabajamos con clases, hay que utilizar: Upper Camel Case 
(primera letra de cada palabra en mayúscula)

El inicializador es init que define los valores iniciales de la clase (init es una función que 
recibe el objeto en sí (self)) y aparte de self puede definir diferentes parámetros.
Hay que asignar esos valores: self.name (se suele dar el mismo nombre a las variables)
"""

class Programmer:

    # Crear un atributo fuera de init (opcional)
    surname: str = None

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages


# Las funciones de una clase deben acabar recibiéndose a sí mismo (self), para poder
#interactuar con los parámetros de la clase (name, age...), que son propiedades de la clase
        
    def print(self):
        print(f"Nombre: {self.name} |Apellidos: {self.surname} | Edad: {self.age} | Languages: {self.languages}")


# Instanciar la clase/crear objeto:
my_programmer = Programmer("Prueba", 54, ["Python", "Java", "Javascript"])

# Llamar a la función de la clase:
my_programmer.print()

# Modificar un parámetro de la clase:
my_programmer.age = 67
my_programmer.print()

