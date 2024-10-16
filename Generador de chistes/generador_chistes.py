from chistes_api import ChistesAPI


def main():
    api = ChistesAPI()  # Crea una instancia de ChistesAPI
    continuar = True  # Flag para controlar el bucle
    print("Vamos a reírnos y calificar los chistes del generador.")

    while continuar:
        chistes = []
        try:
            cantidad = int(input("¿Cuántos chistes quieres en esta ronda?\n"))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un número positivo.")
        except ValueError as e:
            print(f"Error de entrada: {e}")
            continue  # Vuelve a preguntar cuántos chistes quiere

        for i in range(cantidad):
            try:
                chiste = api.obtener_chiste()
                if chiste:
                    print(f"Chiste: {chiste}")
                    nota_valida = False
                    while not nota_valida:
                        try:
                            nota = int(input("🤣 ¿Qué nota le ponemos (0-10)?\n"))
                            if nota < 0 or nota > 10:
                                raise ValueError("La nota debe estar entre 0 y 10.")
                            chistes.append((chiste, nota))
                            nota_valida = True
                        except ValueError as e:
                            print(f"Error de entrada: {e}")
                            continue # Vuelve a preguntar la nota
                else:
                    print("No se pudo obtener un chiste en este momento.\n")
            except Exception as e:
                print(f"Ocurrió un error al obtener el chiste: {e}")

        if chistes:
            # Ordena los chistes por la nota (de mayor a menor)
            chistes_ordenados = sorted(chistes, key=lambda x: x[1], reverse=True)
            try:
                # Calcula la media de notas
                notas = sum([chiste[1] for chiste in chistes])
                media = notas / cantidad
            except ZeroDivisionError:
                media = 0
            print(f"La ronda ha contado con {cantidad} chistes. La media de nota ha sido {media:.2f}. "
                  f"El chiste mejor valorado, con un {chistes_ordenados[0][1]}, ha sido el siguiente:\n"
                  f"{chistes_ordenados[0][0]}")

        try:
            decision = input("¿Quieres otra ronda de chistes? (S/N): ").strip().upper()
            continuar = decision == 'S'
        except ValueError as e:
            print(f"Error de entrada: {e}")
            continuar = False


if __name__ == "__main__":
    main()


