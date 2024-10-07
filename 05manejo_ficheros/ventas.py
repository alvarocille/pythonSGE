# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# Manejo de ficheros

import os
from funciones import *
from config import FICHERO

salir = False

while not salir:
    print(f"Escoge una opción:\n"
          "1. Añadir producto\n"
          "2. Consultar producto\n"
          "3. Actualizar producto\n"
          "4. Borrar producto\n"
          "5. Mostrar todos los productos\n"
          "6. Calcular venta total\n"
          "7. Calcular venta por producto\n"
          "8. Salir")
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    match opcion:
        case 1:  # Añadir producto
            nombre = input("Nombre: ")
            precio = input("Precio: ")
            cantidad = input("Cantidad: ")
            with open(FICHERO, "a") as f:
                f.write(f"{nombre}, {precio}, {cantidad}\n")
            print(f"Producto '{nombre}' añadido.")
            
        case 2:  # Consultar producto
            nombre = pedirProducto()
            productos = listarProductos()
            producto = buscarProducto(productos, nombre)
            if producto:
                print(f"Producto encontrado: {producto}")
            else:
                print("Producto no encontrado.")
                
        case 3:  # Actualizar producto
            nombre = pedirProducto()
            productos = listarProductos()
            indice = buscarIndiceProducto(productos, nombre)
            if indice is not None:
                print("Nuevo nombre (deja en blanco para no cambiar):")
                nuevo_nombre = input() or productos[indice][0]
                print("Nuevo precio (deja en blanco para no cambiar):")
                nuevo_precio = input() or productos[indice][1]
                print("Nueva cantidad (deja en blanco para no cambiar):")
                nueva_cantidad = input() or productos[indice][2]

                productos[indice] = [nuevo_nombre, nuevo_precio, nueva_cantidad]

                with open(FICHERO, "w") as f:
                    for producto in productos:
                        f.write(", ".join(producto) + "\n")
                print(f"Producto '{nombre}' actualizado.")
            else:
                print("Producto no encontrado.")
                
        case 4:  # Borrar producto
            nombre = pedirProducto()
            productos = listarProductos()
            indice = buscarIndiceProducto(productos, nombre)
            if indice is not None:
                productos.pop(indice)
                
                with open(FICHERO, "w") as f:
                    for producto in productos:
                        f.write(", ".join(producto) + "\n")
                print(f"Producto '{nombre}' borrado.")
            else:
                print("Producto no encontrado.")
                
        case 5:  # Mostrar todos los productos
            productos = listarProductos()
            if productos:
                for producto in productos:
                    print(f"Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")
            else:
                print("No hay productos disponibles.")
                
        case 6:  # Calcular venta total
            productos = listarProductos()
            suma = 0
            for producto in productos:
                suma += int(producto[1]) * int(producto[2])
            print(f"Valor total de las ventas: {suma}")
            
        case 7:  # Calcular venta por producto
            nombre = pedirProducto()
            productos = listarProductos()
            producto = buscarProducto(productos, nombre)
            if producto:
                suma = int(producto[1]) * int(producto[2])
                print(f"Valor total de {producto[0]}: {suma}")
            else:
                print("Producto no encontrado.")
                
        case 8:  # Salir del programa
            salir = True
            
        case _:  # Opción incorrecta
            print("Escoge una opción correcta.")

print("Finalizando programa...")
