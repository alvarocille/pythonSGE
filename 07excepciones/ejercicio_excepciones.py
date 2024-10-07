"""
TÍTULO DEL PROGRAMA:
"""
# Comentario:
class StrTypeError(Exception):
    pass


def process_params(parameters: list):
        
    if len(parameters) < 3:
        raise IndexError() # Comentario:
    elif parameters[1] == 0:
        raise ZeroDivisionError() # Comentario:
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto") # Comentario:
    
    print(parameters[2]) # Comentario: 
    print(parameters[0]/parameters[1]) # Comentario:
    print(parameters[2]+5)


try:   
    process_params([23, 2, 2, 45])
except IndexError as e: # Comentario:
    print("La lista debe tener más de 2 elementos")
except ZeroDivisionError as e: # Comentario:
    print("El segundo elemento de la lista no puede ser cero")
except StrTypeError as e: # Comentario:
    print(f"{e}")
except Exception as e: # Comentario:
    print(f"Se ha producido un error inesperado: {e}")
else: # Comentario:
    print("No se ha producido ningún error")
finally: ## Comentario:
    print("El programa finaliza sin detenerse")


print("Fin del programa")



