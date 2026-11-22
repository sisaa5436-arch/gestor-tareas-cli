"""Gestor de tareas por consola."""

AYUDA_MENU = "Elige una opción del menú."


def mostrar_menu():
    print("\nGestor de tareas")
    print(AYUDA_MENU)

    print("0. Salir")


def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()
        if opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nHasta luego.")
