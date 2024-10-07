# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# JSON (JavaScript Object Notation) es un formato de texto ligero para el intercambio de datos.
# Se utiliza comúnmente para almacenar y transportar datos entre un servidor y una aplicación web.
# 
# Características de JSON:
# - Sintaxis fácil de leer y escribir.
# - Estructura basada en pares clave-valor.
# - Puede representar estructuras de datos complejas como objetos y arrays.
# - Es un formato independiente del lenguaje, aunque se deriva de JavaScript.
#
# Usos principales:
# - Almacenar datos de configuración.
# - Intercambiar datos entre cliente y servidor en aplicaciones web.
# - Serializar estructuras de datos en aplicaciones.

import json
import os

# Datos a guardar en el archivo JSON
data = {
    "Nombre": "Alvaro",
    "Edad": 21,
    "Fecha_nacimiento": "2002-12-11",
    "Modulos": ["Python", "Java", "JavaScript"]
}

# Crear y guardar el fichero JSON
file_path = 'datos.json'
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Mostrar el contenido del fichero JSON
with open(file_path, 'r') as json_file:
    contenido = json_file.read()
    print("Contenido del archivo JSON:")
    print(contenido)

# Borrar el fichero JSON
os.remove(file_path)
print(f"\nEl archivo '{file_path}' ha sido borrado.")
