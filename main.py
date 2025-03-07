import tkinter as tk
from tkinter import messagebox

# Función para validar que la entrada sea un número entero entre 0 y 10
def validar_entrada(texto):
    if texto.isdigit():
        valor = int(texto)
        return 0 <= valor <= 10
    elif texto == "":
        return True
    else:
        return False

# Función que se ejecuta al presionar el botón "Calcular"
def calcular():
    nombre = entry_nombre.get().strip()
    if not nombre:
        messagebox.showwarning("Advertencia", "Por favor, ingrese su nombre.")
        return

    try:
        matematicas = int(entry_matematicas.get())
        programacion = int(entry_programacion.get())
        gestion = int(entry_gestion.get())
    except ValueError:
        messagebox.showwarning("Advertencia", "Todos los campos de interés deben tener un valor entre 0 y 10.")
        return

    # Aquí puedes agregar la lógica que desees con los valores ingresados
    resultado = (matematicas + programacion + gestion) / 3
    messagebox.showinfo("Resultado", f"Hola, {nombre}.\nTu promedio de interés es: {resultado:.2f}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Grado de aptitud para ingeniería informática")
root.geometry("500x380")

# Validación de entrada
vcmd = (root.register(validar_entrada), '%P')

# Campo para el nombre
tk.Label(root, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady=5)

# Texto adicional antes de los 3 campos numéricos
tk.Label(root, text="Ingrese el grado de interés en las siguientes áreas:", font=("Arial", 10, "bold")).pack(pady=10)

# Campo para Matemáticas
tk.Label(root, text="Interés en Matemáticas (0-10):").pack(pady=5)
entry_matematicas = tk.Entry(root, validate='key', validatecommand=vcmd)
entry_matematicas.pack(pady=5)

# Campo para Programación
tk.Label(root, text="Interés en Programación (0-10):").pack(pady=5)
entry_programacion = tk.Entry(root, validate='key', validatecommand=vcmd)
entry_programacion.pack(pady=5)

# Campo para Gestión de Proyectos
tk.Label(root, text="Interés en Gestión de Proyectos (0-10):").pack(pady=5)
entry_gestion = tk.Entry(root, validate='key', validatecommand=vcmd)
entry_gestion.pack(pady=5)

# Botón Calcular
tk.Button(root, text="Calcular", command=calcular).pack(pady=10)

# Botón Cerrar
tk.Button(root, text="Cerrar", command=root.quit).pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
