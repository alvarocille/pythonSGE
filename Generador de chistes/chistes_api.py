import requests

class ChistesAPI:
    def __init__(self):
        # URL de la API de chistes en la categoría de programación y en español
        self.url = "https://v2.jokeapi.dev/joke/Programming?lang=es"

    def obtener_chiste(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Lanza un error si la respuesta no es 200
            data = response.json()  # Convierte la respuesta a JSON
            
            # Verifica el tipo de chiste y devuelve el chiste adecuado
            if data['type'] == 'single':
                return data['joke']  # Chiste simple
            elif data['type'] == 'twopart':
                return f"{data['setup']} - {data['delivery']}"  # Chiste de dos partes
        except requests.exceptions.HTTPError as err:
            print(f"Error HTTP: {err}")
        except requests.exceptions.Timeout:
            print("La solicitud ha tardado demasiado. Por favor, inténtalo de nuevo.")
        except requests.exceptions.ConnectionError:
            print("Error de conexión. Verifica tu conexión a Internet.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

# Nota: Se puede añadir un método para gestionar los límites de peticiones aquí si la API los tiene.

