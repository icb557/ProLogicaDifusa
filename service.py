import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

matematicas = ctrl.Antecedent(np.arange(0, 11, 0.1), 'matematicas')
programacion = ctrl.Antecedent(np.arange(0, 11, 0.1), 'programacion')
gestion_de_proyectos = ctrl.Antecedent(np.arange(0, 11, 0.1), 'gestion_de_proyectos')
ingenieria_informatica = ctrl.Consequent(np.arange(0, 11, 0.1), 'ingenieria_informatica')

#configutar membership function -- Matematicas
matematicas['bajo'] = fuzz.trapmf(matematicas.universe, [0, 0, 4, 6])
matematicas['medio'] = fuzz.trapmf(matematicas.universe, [5, 6, 7, 8])
matematicas['alto'] = fuzz.trapmf(matematicas.universe, [7, 8, 10, 10])

# Programación
programacion['bajo'] = fuzz.trapmf(programacion.universe, [0, 0, 4, 6])
programacion['medio'] = fuzz.trapmf(programacion.universe, [5, 6, 7, 8])
programacion['alto'] = fuzz.trapmf(programacion.universe, [7, 8, 10, 10])

# Gestión de Proyectos
gestion_de_proyectos['bajo'] = fuzz.trapmf(gestion_de_proyectos.universe, [0, 0, 4, 6])
gestion_de_proyectos['medio'] = fuzz.trapmf(gestion_de_proyectos.universe, [5, 6, 7, 8])
gestion_de_proyectos['alto'] = fuzz.trapmf(gestion_de_proyectos.universe, [7, 8, 10, 10])


# Ingeniería Informática (Salida)
ingenieria_informatica['No apto'] = fuzz.trapmf(ingenieria_informatica.universe, [0, 0, 4, 6])
ingenieria_informatica['Medianamente apto'] = fuzz.trapmf(ingenieria_informatica.universe, [5, 6, 7, 8])
ingenieria_informatica['Apto'] = fuzz.trapmf(ingenieria_informatica.universe, [7, 8, 10, 10])

rules = [
    # 📌 Combinaciones con matemáticas BAJO
    ctrl.Rule(matematicas['bajo'] & programacion['bajo'] & gestion_de_proyectos['bajo'], ingenieria_informatica['No apto']),
    ctrl.Rule(matematicas['bajo'] & programacion['bajo'] & gestion_de_proyectos['medio'], ingenieria_informatica['No apto']),
    ctrl.Rule(matematicas['bajo'] & programacion['bajo'] & gestion_de_proyectos['alto'], ingenieria_informatica['No apto']),
    ctrl.Rule(matematicas['bajo'] & programacion['medio'] & gestion_de_proyectos['bajo'], ingenieria_informatica['No apto']),
    ctrl.Rule(matematicas['bajo'] & programacion['medio'] & gestion_de_proyectos['medio'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['bajo'] & programacion['medio'] & gestion_de_proyectos['alto'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['bajo'] & programacion['alto'] & gestion_de_proyectos['bajo'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['bajo'] & programacion['alto'] & gestion_de_proyectos['medio'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['bajo'] & programacion['alto'] & gestion_de_proyectos['alto'], ingenieria_informatica['Medianamente apto']),

    # 📌 Combinaciones con matemáticas MEDIO
    ctrl.Rule(matematicas['medio'] & programacion['bajo'] & gestion_de_proyectos['bajo'], ingenieria_informatica['No apto']),
    ctrl.Rule(matematicas['medio'] & programacion['bajo'] & gestion_de_proyectos['medio'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['medio'] & programacion['bajo'] & gestion_de_proyectos['alto'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['medio'] & programacion['medio'] & gestion_de_proyectos['bajo'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['medio'] & programacion['medio'] & gestion_de_proyectos['medio'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['medio'] & programacion['medio'] & gestion_de_proyectos['alto'], ingenieria_informatica['Apto']),
    ctrl.Rule(matematicas['medio'] & programacion['alto'] & gestion_de_proyectos['bajo'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['medio'] & programacion['alto'] & gestion_de_proyectos['medio'], ingenieria_informatica['Apto']),
    ctrl.Rule(matematicas['medio'] & programacion['alto'] & gestion_de_proyectos['alto'], ingenieria_informatica['Apto']),

    # 📌 Combinaciones con matemáticas ALTO
    ctrl.Rule(matematicas['alto'] & programacion['bajo'] & gestion_de_proyectos['bajo'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['alto'] & programacion['bajo'] & gestion_de_proyectos['medio'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['alto'] & programacion['bajo'] & gestion_de_proyectos['alto'], ingenieria_informatica['Apto']),
    ctrl.Rule(matematicas['alto'] & programacion['medio'] & gestion_de_proyectos['bajo'], ingenieria_informatica['Medianamente apto']),
    ctrl.Rule(matematicas['alto'] & programacion['medio'] & gestion_de_proyectos['medio'], ingenieria_informatica['Apto']),
    ctrl.Rule(matematicas['alto'] & programacion['medio'] & gestion_de_proyectos['alto'], ingenieria_informatica['Apto']),
    ctrl.Rule(matematicas['alto'] & programacion['alto'] & gestion_de_proyectos['bajo'], ingenieria_informatica['Apto']),
    ctrl.Rule(matematicas['alto'] & programacion['alto'] & gestion_de_proyectos['medio'], ingenieria_informatica['Apto']),
    ctrl.Rule(matematicas['alto'] & programacion['alto'] & gestion_de_proyectos['alto'], ingenieria_informatica['Apto']),
]

# Definir el sistema de control
ingenieria_ctrl = ctrl.ControlSystem(rules)
ingenieria_simulador = ctrl.ControlSystemSimulation(ingenieria_ctrl)

# Pedir valores de entrada al usuario
valorMatematicas = np.double(input("Ingrese su nivel en matemáticas (0-10): "))
valorProgramacion = np.double(input("Ingrese su nivel en programación (0-10): "))
valorGestionProyectos = np.double(input("Ingrese su nivel en gestión de proyectos (0-10): "))

# Asignar los valores a la simulación
ingenieria_simulador.input['matematicas'] = valorMatematicas
ingenieria_simulador.input['programacion'] = valorProgramacion
ingenieria_simulador.input['gestion_de_proyectos'] = valorGestionProyectos

# Computar el resultado
ingenieria_simulador.compute()

# Obtener el resultado de la salida
resultado = ingenieria_simulador.output['ingenieria_informatica']
print("Nivel de aptitud para Ingeniería Informática:", resultado)

# Mostrar la vista de la salida con la simulación aplicada
ingenieria_informatica.view(sim=ingenieria_simulador)

matematicasBajo = fuzz.interp_membership(matematicas.universe, matematicas['bajo'].mf, valorMatematicas)
matematicasMedio = fuzz.interp_membership(matematicas.universe, matematicas['medio'].mf, valorMatematicas)
matematicasAlto = fuzz.interp_membership(matematicas.universe, matematicas['alto'].mf, valorMatematicas)


programacionBajo = fuzz.interp_membership(programacion.universe, programacion['bajo'].mf, valorProgramacion)
programacionMedio = fuzz.interp_membership(programacion.universe, programacion['medio'].mf, valorProgramacion)
programacionAlto = fuzz.interp_membership(programacion.universe, programacion['alto'].mf, valorProgramacion)

gestionBajo = fuzz.interp_membership(gestion_de_proyectos.universe, gestion_de_proyectos['bajo'].mf, valorGestionProyectos)
gestionMedio = fuzz.interp_membership(gestion_de_proyectos.universe, gestion_de_proyectos['medio'].mf, valorGestionProyectos)
gestionAlto = fuzz.interp_membership(gestion_de_proyectos.universe, gestion_de_proyectos['alto'].mf, valorGestionProyectos)

# Imprimir los valores de pertenencia
print("Matemáticas - Bajo:", matematicasBajo, "Medio:", matematicasMedio, "Alto:", matematicasAlto)
print("Programación - Bajo:", programacionBajo, "Medio:", programacionMedio, "Alto:", programacionAlto)
print("Gestión de Proyectos - Bajo:", gestionBajo, "Medio:", gestionMedio, "Alto:", gestionAlto)
