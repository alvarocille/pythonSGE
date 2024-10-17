from colorama import Fore, Back

def calificar_chiste(chistes_array, chiste_actual):
    try:
        nota = int(input(Fore.MAGENTA + "🤣 ¿Qué nota le ponemos (0-10)?\n"))
        if nota < 0 or nota > 10:
            raise ValueError(Fore.RED + "La nota debe estar entre 0 y 10." + Fore.RESET)
        chistes_array.append((chiste_actual, nota))
        return chistes_array
    except ValueError as e:
        print(Fore.RED + f"Error de entrada: {e}" + Fore.RESET)
        calificar_chiste(chistes_array, chiste_actual)

def clasificar_chistes(chistes_array):
    cantidad = len(chistes_array)
    # Ordena los chistes por la nota (de mayor a menor)
    # La lambda indica que se ordene el array por el segundo parámetro del elemento (nota)
    # Por defecto orden ascendente. Indicamos orden inverso.
    chistes_ordenados = sorted(chistes_array, key=lambda x: x[1], reverse=True)
    try:
        # Calcula la media de notas
        notas = sum([chiste[1] for chiste in chistes_array])
        media = notas / cantidad
    except ZeroDivisionError:
        media = 0
    print(Back.CYAN+Fore.BLACK+ f"La ronda ha contado con {cantidad} chistes. La media de nota ha sido {media:.2f}. "
                                f"El chiste mejor valorado, con un {chistes_ordenados[0][1]}, ha sido el siguiente:"     +Back.RESET+"\n"+
          Back.GREEN+           f"{chistes_ordenados[0][0]}"                                                             +Back.RESET)