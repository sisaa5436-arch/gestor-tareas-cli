"""Gestor de tareas por consola."""

AYUDA_MENU = (
    "Escribe el número de una opción y presiona Enter. "
    "Para completar o eliminar, usa el número del listado."
)


def mostrar_menu():
    print("\nGestor de tareas")
    print(AYUDA_MENU)

    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
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


def pedir_indice(tareas):
    """Devuelve el índice de la tarea seleccionada, si existe."""
    if not tareas:
        print("No hay tareas.")
        return None

    try:
        numero = int(input("Número de tarea: "))
    except ValueError:
        print("Ingresa un número entero.")
        return None

    if not 1 <= numero <= len(tareas):
        print("No existe una tarea con ese número.")
        return None
    return numero - 1


def completar_tarea(tareas):
    indice = pedir_indice(tareas)
    if indice is not None:
        tareas[indice]["completada"] = True
        print("Tarea completada.")


def eliminar_tarea(tareas):
    indice = pedir_indice(tareas)
    if indice is not None:
        tareas.pop(indice)
        print("Tarea eliminada.")


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
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nHasta luego.")
