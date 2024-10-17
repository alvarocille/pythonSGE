from colorama import Fore

def pedir_cantidad():
    try:
        cantidad = int(input(Fore.MAGENTA + "¿Cuántos chistes quieres en esta ronda?\n"))
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un número positivo.")
        return cantidad
    except ValueError as e:
        print(Fore.RED + f"Error de entrada: {e}" + Fore.RESET)
        pedir_cantidad()  # Vuelve a preguntar cuántos chistes quiere con recursividad

def repetir_ronda():
    try:
        decision = input(Fore.MAGENTA + "¿Quieres otra ronda de chistes? (S/N): ").strip().upper()
        return decision == 'S'
    except ValueError as e:
        print(Fore.RED + f"Error de entrada: {e}" + Fore.RESET)
        return False