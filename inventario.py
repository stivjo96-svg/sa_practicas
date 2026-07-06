from config import *
from persistencia import *
from producto import Producto


def validar_producto(producto: Producto):

    return (

        producto.nombre != ""

        and producto.precio > 0

        and producto.stock >= 0

    )


def calcular_iva(precio, categoria):

    if categoria == "Tecnología":

        return precio * 0.12

    return precio * IVA


def calcular_precio_final(producto):

    precio_con_iva = (

        producto.precio

        +

        calcular_iva(

            producto.precio,

            producto.categoria

        )

    )

    if producto.categoria == CATEGORIA_DESCUENTO:

        return precio_con_iva * (

            1 - DESCUENTO_TECNOLOGIA

        )

    return precio_con_iva


def registrar_producto(producto):

    if not validar_producto(producto):

        print("Datos inválidos.")

        return

    precio_final = calcular_precio_final(producto)

    guardar_producto(

        producto,

        precio_final

    )

    print("Producto registrado.")


def listar_productos():

    productos = leer_productos()

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

    total = sum(

        calcular_iva(

            producto["precio"],

            producto["categoria"]

        )

        for producto in productos

    )

    print(

        f"IVA acumulado: ${total:.2f}"

    )