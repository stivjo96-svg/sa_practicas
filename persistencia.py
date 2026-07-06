import os
import json

from config import ARCHIVO_INVENTARIO

def guardar_producto(producto, precio_final):

    nuevo_producto = {
        "codigo_barras": producto.codigo_barras,
        "nombre": producto.nombre,
        "precio": producto.precio,
        "stock": producto.stock,
        "categoria": producto.categoria,
        "precio_final": precio_final
    }

    productos = []

    if os.path.exists(ARCHIVO_INVENTARIO):

        with open(ARCHIVO_INVENTARIO, "r") as archivo:

            try:
                productos = json.load(archivo)

            except:
                productos = []

    productos.append(nuevo_producto)

    with open(ARCHIVO_INVENTARIO, "w") as archivo:

        json.dump(
            productos,
            archivo,
            indent=4
        )


def leer_productos():

    if not os.path.exists(ARCHIVO_INVENTARIO):

        return []

    with open(ARCHIVO_INVENTARIO, "r") as archivo:

        try:
            productos = json.load(archivo)

        except:
            productos = []

    return productos