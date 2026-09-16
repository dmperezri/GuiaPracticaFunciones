# utilerias.py


def leer_float(mensaje):
    while True:

        try:
            return float(input(mensaje))

        except ValueError:
            print("Ingrese un número válido.")


def leer_entero(mensaje):
    while True:

        try:
            return int(input(mensaje))

        except ValueError:
            print("Ingrese un número entero válido.")


def mostrar_titulo(titulo):

    print("\n" + "=" * 50)
    print(titulo.center(50))
    print("=" * 50)


def pausar():
    input("\nPresione Enter para continuar...")