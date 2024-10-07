import os
from config import FICHERO

def pedirProducto():
    print("Introduce el nombre del producto a buscar:")
    return input()

def listarProductos():
    productos = []
    with open(FICHERO, "r") as f:
        lineas = f.read().splitlines()
        for linea in lineas:
            if linea.strip():
                producto = linea.split(", ")
                productos.append(producto)
    return productos

def buscarProducto(productos, nombre):
    for producto in productos:
        if producto[0] == nombre:
            return producto
    return None

def buscarIndiceProducto(productos, nombre):
    for i, producto in enumerate(productos):
        if producto[0] == nombre:
            return i
    return None
