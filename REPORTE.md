# REPORTE DE DEUDA TÉCNICA

## Integrantes

- Stiven Vallejo
- Guillermo Vallejo

---

# 1. Diagnóstico de calidad

Se identificaron los siguientes problemas:

- Función `p_pro()` con demasiadas responsabilidades.
- Uso de valores hardcodeados (IVA 15%).
- Código duplicado.
- Persistencia inicial mediante TXT.
- Variables con nombres poco descriptivos.
- Baja mantenibilidad.

---

# 2. Mapeo de dificultades

## Cambio 1: Alerta de stock bajo

Se agregó una alerta cuando el inventario es menor a 5 unidades.

Impacto:

- Bajo

Archivos modificados:

- main.py

---

## Cambio 2: IVA para Tecnología

Se cambió el IVA de Tecnología al 12%.

Impacto:

- Medio

Fue necesario modificar:

- cálculo de IVA
- reporte de IVA

---

## Cambio 3: Migración a JSON

Se sustituyó el almacenamiento TXT por JSON.

Impacto:

- Alto

Fue necesario modificar:

- escritura
- lectura
- reportes
- persistencia

---

## Cambio 4: Código de barras

Se añadió el atributo obligatorio `codigo_barras`.

Impacto:

- Medio

Se modificó:

- función principal
- JSON
- listado
- registros de prueba

---

# 3. Refactorizaciones propuestas

- Separar responsabilidades de `p_pro()`.
- Crear una clase `Producto`.
- Centralizar el cálculo del IVA.
- Implementar una capa de persistencia.
- Utilizar constantes globales.

---

# 4. Conclusiones

El sistema presenta deuda técnica debido a:

- Código duplicado
- Valores hardcodeados
- Alta dependencia entre módulos

La migración a JSON mejoró la mantenibilidad del sistema.

La incorporación del código de barras evidencia la dificultad de evolucionar sistemas con deuda técnica acumulada.

---

## Repositorio

https://github.com/stivjo96-svg/sa_practicas