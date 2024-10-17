from traceback import print_exception, print_exc

import requests
from colorama import Fore, Back
from config import TEMAS_DISPONIBLES, IDIOMAS_DISPONIBLES

class ChistesAPI:
    def __init__(self, tema, idioma):
            if tema not in TEMAS_DISPONIBLES:
                raise ValueError(Back.RED + Fore.BLACK + f"Tema '{tema}' no es válido. Los temas disponibles son: {', '.join(TEMAS_DISPONIBLES)}" + Back.RESET + Fore.RESET)
            if idioma not in IDIOMAS_DISPONIBLES:
                raise ValueError(Back.RED + Fore.BLACK + f"Idioma '{idioma}' no es válido. Los idiomas disponibles son: {', '.join(IDIOMAS_DISPONIBLES)}" + Back.RESET + Fore.RESET)

            self.chiste = None
            # URL de la API de chistes
            self.url = f"https://v2.jokeapi.dev/joke/{tema}?lang={idioma}"

    def obtener_chiste(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Lanza un error si la respuesta no es 200
            data = response.json()  # Convierte la respuesta a JSON
            if data['error']:
                print(Fore.RED + "No hay chistes disponibles." + Fore.RESET)
            else:
                # Verifica el tipo y devuelve el chiste con sintaxis adecuada
                if data['type'] == 'single':
                    self.chiste = data['joke']  # Chiste simple
                elif data['type'] == 'twopart':
                    self.chiste = f"{data['setup']} - {data['delivery']}"  # Chiste de dos partes


        except requests.exceptions.HTTPError as err:
            print(Fore.RED+f"Error HTTP: {err}"+Fore.RESET)
        except requests.exceptions.Timeout:
            print(Fore.RED+"La solicitud ha tardado demasiado. Por favor, inténtalo de nuevo."+Fore.RESET)
        except requests.exceptions.ConnectionError:
            print(Fore.RED+"Error de conexión. Verifica tu conexión a Internet."+Fore.RESET)
        except Exception as e:
            print(Fore.RED+f"Ocurrió un error: {e}"+Fore.RESET)

