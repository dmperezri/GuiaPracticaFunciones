# principal.py

import retos
import utilerias

def main():

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        )

        if opcion == "1":
            ejercicio_1()

        elif opcion == "2":
            ejercicio_2()

        elif opcion == "3":
            ejercicio_3()

        elif opcion == "4":
            ejercicio_4()

        elif opcion == "5":
            ejercicio_5()

        elif opcion == "6":
            ejercicio_6()

        elif opcion == "7":
            ejercicio_7()

        elif opcion == "0":

            print("\nPrograma finalizado.")
            break

        else:

            print(
                "\nOpción no válida."
            )

        utilerias.pausar()

# ==================================================
# TEMA 1
# ==================================================

def ejercicio_1():

    utilerias.mostrar_titulo(
        "VARIABLE GLOBAL - NOMBRE DE EMPRESA"
    )

    print("La variable nombre_empresa fue declarada")
    print("fuera de las funciones.\n")

    empresa = retos.mostrar_empresa()

    print("Nombre de la empresa:", empresa)


def ejercicio_2():

    utilerias.mostrar_titulo(
        "VARIABLE LOCAL - TOTAL"
    )

    total = retos.crear_total()

    print("La función creó una variable local llamada total.")
    print("Valor devuelto:", total)

    print("\nLa variable que existe dentro de crear_total()")
    print("no puede utilizarse directamente fuera de esa función.")

    print("\nPor ejemplo:")

    print("""
def crear_total():
    total = 2500

print(total)
""")

    print("Esto produciría:")
    print("NameError: name 'total' is not defined")


def ejercicio_3():

    utilerias.mostrar_titulo(
        "CONTADOR GLOBAL"
    )

    print("Contador actual:", retos.obtener_contador())

    retos.incrementar_contador()

    print("Después de llamar la función:")
    print("Contador:", retos.obtener_contador())

    retos.incrementar_contador()

    print("\nDespués de llamarla nuevamente:")
    print("Contador:", retos.obtener_contador())


# ==================================================
# TEMA 2
# ==================================================

def ejercicio_4():

    utilerias.mostrar_titulo(
        "PARÁMETRO INMUTABLE - SALARIO"
    )

    salario = utilerias.leer_float(
        "Ingrese el salario: C$ "
    )

    print("\nSalario original:", salario)

    nuevo_salario = retos.aumentar_salario(salario)

    print("Salario dentro de la función:", nuevo_salario)

    print("Salario original después de la función:", salario)

    print("\nConclusión:")
    print("El salario original no cambió porque")
    print("los números son objetos inmutables.")


def ejercicio_5():

    utilerias.mostrar_titulo(
        "PARÁMETRO MUTABLE - LISTA"
    )

    ventas = [1200, 1500, 850]

    print("Lista original:")
    print(ventas)

    nueva_venta = utilerias.leer_float(
        "\nIngrese una nueva venta: C$ "
    )

    retos.agregar_venta(
        ventas,
        nueva_venta
    )

    print("\nLista después de llamar la función:")
    print(ventas)

    print("\nLa lista original cambió porque")
    print("las listas son objetos mutables.")


def ejercicio_6():

    utilerias.mostrar_titulo(
        "INMUTABLE VS MUTABLE"
    )

    salario = 5000

    ventas = [
        1000,
        2000
    ]

    print("ANTES")
    print("Salario:", salario)
    print("Ventas:", ventas)

    salario_modificado = retos.aumentar_salario(
        salario
    )

    retos.agregar_venta(
        ventas,
        3000
    )

    print("\nDESPUÉS")

    print("Salario original:", salario)

    print(
        "Salario modificado dentro de la función:",
        salario_modificado
    )

    print("Ventas:", ventas)

    print("\nEXPLICACIÓN")

    print(
        "El salario no cambia porque int y float "
        "son objetos inmutables."
    )

    print(
        "La lista sí cambia porque list es un "
        "objeto mutable y append modifica su contenido."
    )


# ==================================================
# TEMA 3
# ==================================================

def ejercicio_7():

    utilerias.mostrar_titulo(
        "FUNCIONES Y PROCEDIMIENTOS"
    )

    precio = utilerias.leer_float(
        "Precio unitario: C$ "
    )

    cantidad = utilerias.leer_entero(
        "Cantidad: "
    )

    subtotal = retos.calcular_subtotal(
        precio,
        cantidad
    )

    descuento = retos.calcular_descuento(
        subtotal
    )

    monto_con_descuento = (
        subtotal - descuento
    )

    iva = retos.calcular_iva(
        monto_con_descuento
    )

    total = retos.calcular_total(
        subtotal,
        descuento,
        iva
    )

    retos.mostrar_resumen(
        subtotal,
        descuento,
        iva,
        total
    )


def mostrar_menu():

    print("""
==================================================
        PRÁCTICA DE FUNCIONES EN PYTHON
==================================================
    1. Variable global nombre_empresa
    2. Variable local total
    3. Contador global
    ------------------------------------------
    4. Parámetro inmutable - salario
    5. Parámetro mutable - lista de ventas
    6. Comparar mutable e inmutable
    ------------------------------------------
    7. Venta de una distribuidora
    0. Salir
==================================================
    """)





if __name__ == "__main__":
    main()