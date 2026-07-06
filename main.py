from producto import Producto

from inventario import *


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