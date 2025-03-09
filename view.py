import tkinter as tk
from tkinter import messagebox
from service import getResults

# Función para validar que la entrada sea un número entero entre 0 y 10
def validar_entrada(texto):
    if texto.isdigit():
        valor = int(texto)
        return 0 <= valor <= 10
    elif texto == "":
        return True
    else:
        return False

# Función para mostrar el formulario
def show_form():
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
        resultados = getResults(matematicas, programacion, gestion)
        messagebox.showinfo("Resultado", 
                            f"""Hola, {nombre}.
                            \nSegún tu grado de interés en las áreas solicitadas eres: {resultados['resultadoTexto']} para estudiar Ingeniería Informática.
                            \n\nDetalles adicionales:
                            \n  - Nivel de aptitud: {resultados['resultadoNumerico']:.2f}/10
                            \n  - Pertenencia a conjuntos antecedentes:
                            \n     - Matemáticas: 
                            \n          - Bajo: {resultados['membership']['Antecedentes']['matematicas']['bajo']:.2f}
                            \n          - Medio: {resultados['membership']['Antecedentes']['matematicas']['medio']:.2f}
                            \n          - Alto: {resultados['membership']['Antecedentes']['matematicas']['alto']:.2f}
                            \n     - Programación:
                            \n          - Bajo: {resultados['membership']['Antecedentes']['programacion']['bajo']:.2f}
                            \n          - Medio: {resultados['membership']['Antecedentes']['programacion']['medio']:.2f}
                            \n          - Alto: {resultados['membership']['Antecedentes']['programacion']['alto']:.2f}
                            \n     - Gestión de Proyectos:
                            \n          - Bajo: {resultados['membership']['Antecedentes']['gestion_de_proyectos']['bajo']:.2f}
                            \n          - Medio: {resultados['membership']['Antecedentes']['gestion_de_proyectos']['medio']:.2f}
                            \n          - Alto: {resultados['membership']['Antecedentes']['gestion_de_proyectos']['alto']:.2f}
                            \n  - Pertenencia a conjuntos consecuentes:
                            \n     - No apto: {resultados['membership']['Consecuente']['No apto']:.2f}
                            \n     - Medianamente apto: {resultados['membership']['Consecuente']['Medianamente apto']:.2f}
                            \n     - Apto: {resultados['membership']['Consecuente']['Apto']:.2f}""")

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
