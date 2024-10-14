from chistes_api import ChistesAPI

def main():
    api = ChistesAPI()  # Crea una instancia de ChistesAPI
    continuar = True  # Flag para controlsar el bucle
    print("Vamos a reírnos y calificar los chistes del generador.")
    while continuar:
        chistes = []
        cantidad = int(input("¿Cuántos chistes quieres en esta ronda?"))
        for i in range(1,cantidad):
            chiste = api.obtener_chiste()  # Obtiene un chiste de la API
            if chiste:
                print(f"Chiste: {chiste}")  # Muestra el chiste
                nota = input("🤣 ¿Qué nota le ponemos?")
                chistes.append((chiste, nota))
            else:
                print("No se pudo obtener un chiste en este momento.")  # Mensaje en caso de error
        chistes_ordenados = sorted(chistes, key=lambda x: x[1], reverse=True)
        for chiste, nota in chistes_ordenados:
            print(f"Chiste: {chiste} | Nota: {nota}")
    # Pregunta al usuario si desea continuar
    decision = input("¿Quieres otra ronda de chistes? (S/N): ").strip().upper()
    continuar = decision == 'S'  # Actualiza la bandera según la decisión del usuario

if __name__ == "__main__":
    main()

