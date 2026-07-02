import os
import json

# Archivo de texto para persistencia de datos
A = "inventario.json"

def p_pro(op, x, p, c, t):
    # Función gigante que hace absolutamente todo: valida, calcula, escribe y formatea
    if op == 1:
        # VALIDACIÓN Y REGISTRO DE PRODUCTO
        if x == "" or p <= 0 or c < 0:
            print("Error: Datos inválidos.")
            return False
        
        # Hardcoding: IVA del 15% quemado directamente en el bucle/lógica
        if t == "Tecnología":
            iva = p * 0.12
        else:
            iva = p * 0.15

        total_con_iva = p + iva
        
        # Lógica de descuento repetida e idéntica (Código duplicado)
        if t == "Tecnología":
            # 10% de descuento para tecnología
            p_final = total_con_iva - (total_con_iva * 0.10)
        else:
            p_final = total_con_iva
            
        producto = {
            "nombre": x,
            "precio": p,
            "stock": c,
            "categoria": t,
            "precio_final": p_final
        }

        if os.path.exists(A):
            with open(A, "r") as f:
                productos = json.load(f)
        else:
            productos = []

        productos.append(producto)

        with open(A, "w") as f:
            json.dump(productos, f, indent=4)

        print("Producto guardado con éxito.")
        
    elif op == 2:
        # LECTURA Y DESPLIEGUE EN TABLA
        if not os.path.exists(A):
            print("No hay datos registrados.")
            return

        with open(A, "r") as f:
            productos = json.load(f)

        print("--------------------------------------------------")
        print("PROD | PRECIO | STOCK | CAT | PRECIO FINAL")
        print("--------------------------------------------------")

        for producto in productos:

            x1 = producto["nombre"]
            p1 = producto["precio"]
            c1 = producto["stock"]
            t1 = producto["categoria"]
            pf1 = producto["precio_final"]

            print(f"{x1} | ${p1} | {c1} unidades | {t1} | ${pf1}")

            if c1 < 5:
                print("⚠ ALERTA: Stock bajo")

        print("--------------------------------------------------")

    elif op == 3:

        if not os.path.exists(A):
            return

        with open(A, "r") as f:
            productos = json.load(f)

        sumatoria = 0

        for producto in productos:

            precio_base = producto["precio"]

            if producto["categoria"] == "Tecnología":
                iva_repetido = precio_base * 0.12
            else:
                iva_repetido = precio_base * 0.15

            sumatoria += iva_repetido

        print(f"Total de IVA acumulado en inventario: ${sumatoria}")

# Simulación de ejecución del programa
if __name__ == "__main__":
    print("--- SISTEMA DE INVENTARIO VIEJO V1.0 ---")
    # Registrar un par de productos de prueba
    p_pro(1, "Laptop", 800.0, 3, "Tecnología")
    p_pro(1, "Cuaderno", 2.50, 50, "Útiles")
    
    # Listar productos
    p_pro(2, "", 0, 0, "")
    
    # Ver reporte de IVA
    p_pro(3, "", 0, 0, "")
