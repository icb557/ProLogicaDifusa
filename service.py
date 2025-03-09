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

def calcMembership(funcion, valor, conjunto):
    return fuzz.interp_membership(funcion.universe, funcion[conjunto].mf, valor)

def deffuzifyResult(resultado, ingInfNoApto, ingInfMedioApto, ingInfApto):
    # Determinar la clasificación final
    if resultado <= 4:
        clasificacion = "No Apto"
    elif resultado >= 5 and resultado <=6:
        Mayor = np.fmax(ingInfNoApto, ingInfMedioApto)
        if Mayor == ingInfNoApto:
            clasificacion = "No Apto"
        else:
            clasificacion = "Medianamente Apto"
    elif resultado >= 7 and resultado <=8:
        Mayor = np.fmax(ingInfMedioApto, ingInfApto)
        if Mayor == ingInfMedioApto:
            clasificacion = "Medianamente Apto"
        else:
            clasificacion = "Apto"
    else:
        clasificacion = "Apto"
    return clasificacion

def getResults(valorMatematicas, valorProgramacion, valorGestionProyectos):
    # Asignar los valores a la simulación
    ingenieria_simulador.input['matematicas'] = valorMatematicas
    ingenieria_simulador.input['programacion'] = valorProgramacion
    ingenieria_simulador.input['gestion_de_proyectos'] = valorGestionProyectos

    # Computar el resultado
    ingenieria_simulador.compute()

    # Obtener el resultado de la salida
    resultado = ingenieria_simulador.output['ingenieria_informatica']   

    membership = {
        "Antecedentes": {
            "matematicas": {
                "bajo": calcMembership(matematicas, valorMatematicas, 'bajo'),
                "medio": calcMembership(matematicas, valorMatematicas, 'medio'),
                "alto": calcMembership(matematicas, valorMatematicas, 'alto')
            }, 
            "programacion": {
                "bajo": calcMembership(programacion, valorProgramacion, 'bajo'),
                "medio": calcMembership(programacion, valorProgramacion, 'medio'),
                "alto": calcMembership(programacion, valorProgramacion, 'alto')
            }, 
            "gestion_de_proyectos": {
                "bajo": calcMembership(gestion_de_proyectos, valorGestionProyectos, 'bajo'),
                "medio": calcMembership(gestion_de_proyectos, valorGestionProyectos, 'medio'),
                "alto": calcMembership(gestion_de_proyectos, valorGestionProyectos, 'alto')

            }
        },
        "Consecuente": {
            "No apto": calcMembership(ingenieria_informatica, resultado, 'No apto'),
            "Medianamente apto": calcMembership(ingenieria_informatica, resultado, 'Medianamente apto'),
            "Apto": calcMembership(ingenieria_informatica, resultado, 'Apto')
        }
    }

    results = {
        "resultadoNumerico": resultado,
        "resultadoTexto": deffuzifyResult(resultado, membership["Consecuente"]["No apto"], membership["Consecuente"]["Medianamente apto"], membership["Consecuente"]["Apto"]),
        "membership": membership
    }

    return results

