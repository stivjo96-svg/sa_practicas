import os
import json
from dataclasses import dataclass

ARCHIVO_INVENTARIO = "inventario.json"
IVA = 0.15
CATEGORIA_DESCUENTO = "Tecnología"
DESCUENTO_TECNOLOGIA = 0.10

@dataclass
class Producto:
    codigo_barras: str
    nombre: str
    precio: float
    stock: int
    categoria: str

def validar_producto(producto: Producto) -> bool:
    return (
        producto.nombre != ""
        and producto.precio > 0
        and producto.stock >= 0
    )

def calcular_iva(precio: float, categoria: str) -> float:

    if categoria == "Tecnología":
        return precio * 0.12

    return precio * IVA


def calcular_precio_final(producto: Producto) -> float:

    precio_con_iva = (
        producto.precio +
        calcular_iva(
            producto.precio,
            producto.categoria
        )
    )

    if producto.categoria == CATEGORIA_DESCUENTO:
        return precio_con_iva * (1 - DESCUENTO_TECNOLOGIA)

    return precio_con_iva

def guardar_producto(producto: Producto):

    precio_final = calcular_precio_final(producto)

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
        json.dump(productos, archivo, indent=4)

def registrar_producto(producto: Producto):

    if not validar_producto(producto):
        print("Datos inválidos.")
        return

    guardar_producto(producto)
    print("Producto registrado.")

def leer_productos():

    if not os.path.exists(ARCHIVO_INVENTARIO):
        return []

    with open(ARCHIVO_INVENTARIO, "r") as archivo:

        try:
            productos = json.load(archivo)
        except:
            productos = []

    return productos

def listar_productos():

    productos = leer_productos()

    if not productos:
        print("No existen productos.")
        return

    print("-" * 60)

    for producto in productos:
        print(
            f"{producto['codigo_barras']} | "
            f"{producto['nombre']} | "
            f"${producto['precio']} | "
            f"{producto['stock']} | "
            f"{producto['categoria']} | "
            f"${producto['precio_final']:.2f}"
        )
        if producto["stock"] < 5:
            print("⚠ ALERTA: Stock bajo")

def reporte_iva():

    productos = leer_productos()

    total_iva = sum(

        calcular_iva(
            producto["precio"],
            producto["categoria"]
        )

        for producto in productos

    )

    print(f"IVA acumulado: ${total_iva:.2f}")


def main():

    registrar_producto(
        Producto(
            "789456123",
            "Laptop",
            800,
            3,
            "Tecnología"
        )
    )

    registrar_producto(
        Producto(
            "123987654",
            "Cuaderno",
            2.5,
            50,
            "Útiles"
        )
    )

    listar_productos()

    reporte_iva()


if __name__ == "__main__":
    main()