# retos.py

# ==================================================
# TEMA 1: ÁMBITO DE VARIABLES Y FUNCIONES
# ==================================================

nombre_empresa = "Distribuidora El Buen Precio"

contador = 0


def mostrar_empresa():
    """
    Demuestra el uso de una variable global.
    """
    return nombre_empresa


def crear_total():
    """
    Demuestra una variable local.
    """
    total = 2500

    return total


def incrementar_contador():
    """
    Modifica una variable global usando global.
    """
    global contador

    contador += 1

    return contador


def obtener_contador():
    return contador


# ==================================================
# TEMA 2: PASO DE PARÁMETROS
# ==================================================

def aumentar_salario(salario):
    """
    El número es inmutable.
    Reasignar salario no modifica la variable original.
    """

    salario = salario + 500

    return salario


def agregar_venta(ventas, nueva_venta):
    """
    La lista es mutable.
    append modifica la lista original.
    """

    ventas.append(nueva_venta)


# ==================================================
# TEMA 3: FUNCIONES Y PROCEDIMIENTOS
# ==================================================

def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal):

    if subtotal >= 5000:
        return subtotal * 0.10

    return 0


def calcular_iva(monto):
    return monto * 0.15


def calcular_total(subtotal, descuento, iva):
    return subtotal - descuento + iva


def mostrar_resumen(subtotal, descuento, iva, total):
    """
    Procedimiento:
    realiza una acción, pero no devuelve un resultado útil.
    """

    print("\n--- RESUMEN DE VENTA ---")
    print(f"Subtotal: C$ {subtotal:.2f}")
    print(f"Descuento: C$ {descuento:.2f}")
    print(f"IVA: C$ {iva:.2f}")
    print(f"Total: C$ {total:.2f}")