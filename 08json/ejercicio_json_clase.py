# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# Manejo JSON

import json
import os

# Función para generar un fichero JSON con datos de una persona
def crear_fichero_json(nombre, edad, fecha_nacimiento, modulos):
    data = {
        "Nombre": nombre,
        "Edad": edad,
        "Fecha_nacimiento": fecha_nacimiento,
        "Módulos": modulos
    }
    
    file_path = 'datos_persona.json'
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    return file_path

# Clase Person que almacena los atributos de una persona
class Person:
    def __init__(self, nombre, edad, fecha_nacimiento, modulos):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.modulos = modulos
    
    def mostrar_atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Módulos: {', '.join(self.modulos)}")

# Generar el fichero JSON
file_path = crear_fichero_json("Alvaro", 30, "1994-01-01", ["Python", "Java", "JavaScript"])

# Leer el fichero JSON y convertirlo en un objeto de la clase Person
with open(file_path, 'r') as json_file:
    data = json.load(json_file)
    persona = Person(data["Nombre"], data["Edad"], data["Fecha_nacimiento"], data["Módulos"])

# Mostrar los atributos de la instancia de la clase
persona.mostrar_atributos()

# Borrar el fichero JSON
os.remove(file_path)
print(f"\nEl archivo '{file_path}' ha sido borrado.")
