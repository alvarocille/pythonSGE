import traceback
from traceback import print_exception

from chistes_api import ChistesAPI
from colorama import Fore, Back
from manejo_chistes import clasificar_chistes, calificar_chiste
from manejo_secuencia import pedir_cantidad, repetir_ronda

def main():
    try:
        api = ChistesAPI("Programming", "es") # Crea una instancia de ChistesAPI (programación, español)
    except ValueError as e:
        tb = traceback.format_exc(limit=1)  # Solo muestra la traza del archivo principal
        print(Fore.RED + f"ERROR:\n{tb}" + Fore.RESET)
        exit()

    continuar = True  # Flag para controlar el bucle
    print(Fore.YELLOW+"Vamos a reírnos y calificar los chistes del generador.")
    while continuar:
        chistes = []
        cantidad = pedir_cantidad()
        for i in range(cantidad):
            try:
                api.obtener_chiste()
                if api.chiste:
                    print(Fore.RESET+"Chiste: " + Back.MAGENTA+Fore.BLACK+f"{api.chiste}"+Back.RESET+Fore.RESET)
                    calificar_chiste(chistes, api.chiste)
                else:
                    print(Fore.RED+"No se pudo obtener un chiste en este momento.\n"+Fore.RESET)
            except Exception as e:
                print(Fore.RED+f"Ocurrió un error al obtener el chiste: {e}"+Fore.RESET)
        if chistes:
            clasificar_chistes(chistes)
        continuar = repetir_ronda()
    print(Fore.YELLOW+"¡Qué tenga un buen día!")

if __name__ == "__main__":
    main()


