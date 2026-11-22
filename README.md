# Gestor de tareas CLI

Programa de consola en Python para agregar, listar, completar y eliminar tareas.
Cada tarea guarda su título y si está pendiente o completada. Las tareas se
mantienen en memoria durante la ejecución.

## Requisitos

- Python 3.8 o posterior.
- Una terminal. El programa utiliza únicamente la biblioteca estándar.

## Uso

Desde la carpeta del proyecto, ejecuta:

```bash
python app.py
```

Si el comando anterior no está disponible en Linux o macOS, usa
`python3 app.py`. En Windows también puedes usar `py app.py`.

| Opción | Acción |
| --- | --- |
| 1 | Agregar una tarea con un título. |
| 2 | Listar las tareas y ver su estado. |
| 3 | Completar una tarea por su número. |
| 4 | Eliminar una tarea por su número. |
| 0 | Salir del programa. |

Para completar o eliminar una tarea, elige el número que aparece en el
listado. La numeración se actualiza después de cada eliminación. Los títulos
vacíos o compuestos únicamente por espacios se rechazan. Al salir, se borra la
lista de la sesión.
