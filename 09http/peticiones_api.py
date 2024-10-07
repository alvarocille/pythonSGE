# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# Definición de API:
# Una API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y protocolos que permiten la comunicación entre diferentes aplicaciones.
# Permite que los desarrolladores accedan a funcionalidades o datos de un sistema sin conocer su implementación interna.

# Definición de API RESTful:
# Una API RESTful es un tipo de API que sigue los principios de la arquitectura REST (Transferencia de Estado Representacional).
# Utiliza métodos HTTP para acceder y manipular recursos, y generalmente devuelve datos en formato JSON.

# Definición de Endpoint:
# Un endpoint es una URL a la que se puede acceder a través de una API para interactuar con un recurso específico.
# Los endpoints definen la ruta de acceso para realizar peticiones a la API. Por ejemplo, en la API de Pokémon, el endpoint para obtener un Pokémon específico es:
# https://pokeapi.co/api/v2/pokemon/{id o nombre}

import requests

def obtener_informacion_pokemon(nombre_o_numero):
    # Asegurarse de que el nombre del Pokémon está en minúsculas
    nombre_o_numero = nombre_o_numero.lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_o_numero}"

    # Realizar la petición GET
    response = requests.get(url)

    # Controlar errores
    if response.status_code == 200:
        data = response.json()
        # Mostrar los datos del Pokémon
        print(f"Nombre: {data['name']}")
        print(f"ID: {data['id']}")
        print(f"Peso: {data['weight']}")
        print(f"Altura: {data['height']}")
        tipos = [tipo['type']['name'] for tipo in data['types']]
        print(f"Tipos: {', '.join(tipos)}")
    elif response.status_code == 404:
        print("Error: Pokémon no encontrado. Asegúrate de que el nombre o número sea correcto.")
    else:
        print(f"Error inesperado. Código de error: {response.status_code}")

# Ejemplo de uso
if __name__ == "__main__":
    pokemon = input("Introduce el nombre o número de un Pokémon: ")
    obtener_informacion_pokemon(pokemon)
