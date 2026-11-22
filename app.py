"""Gestor de tareas por consola."""

AYUDA_MENU = "Escribe el número de una opción y presiona Enter."


def mostrar_menu():
    print("\nGestor de tareas")
    print(AYUDA_MENU)

    print("1. Agregar tarea")
    print("2. Listar tareas")

    print("0. Salir")


def agregar_tarea(tareas):
    titulo = input("Título: ")
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada.")


def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
        return

    for numero, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f'{numero}. [{estado}] {tarea["titulo"]}')


def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()
        if opcion == "0":
            print("Hasta luego.")
            break
        elif opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nHasta luego.")
