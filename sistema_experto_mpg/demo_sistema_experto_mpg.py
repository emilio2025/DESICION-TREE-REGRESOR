# ============================================================
# SISTEMA EXPERTO - CONSUMO DE COMBUSTIBLE (AUTO MPG)
# Diagnóstico básico de eficiencia de combustible de un vehículo
# ============================================================

# ------------------------------------------------------------
# 1. BASE DE CONOCIMIENTOS
# ------------------------------------------------------------
# Las reglas representan conocimiento proporcionado por
# un experto. Cada regla tiene condiciones y una conclusión.
#
# Formato conceptual:
#
# SI condición_1 Y condición_2
# ENTONCES conclusión
# ------------------------------------------------------------

reglas = [

    {
        "nombre": "Regla 1 - Vehículo pesado con motor grande",
        "condiciones": ["peso_pesado", "motor_grande"],
        "conclusion": "Consumo alto (baja eficiencia / bajo MPG)",
        "recomendacion": "Reducir peso del vehículo, revisar la afinación del motor y evitar aceleraciones bruscas."
    },

    {
        "nombre": "Regla 2 - Vehículo pesado con motor mediano",
        "condiciones": ["peso_pesado", "motor_mediano"],
        "conclusion": "Consumo alto (baja eficiencia / bajo MPG)",
        "recomendacion": "Reducir peso del vehículo y realizar mantenimiento preventivo del motor."
    },

    {
        "nombre": "Regla 3 - Vehículo ligero con motor pequeño",
        "condiciones": ["peso_ligero", "motor_pequeno"],
        "conclusion": "Consumo bajo (alta eficiencia / alto MPG)",
        "recomendacion": "Vehículo eficiente: no se requieren acciones correctivas."
    },

    {
        "nombre": "Regla 4 - Vehículo de peso medio",
        "condiciones": ["peso_medio"],
        "conclusion": "Consumo medio",
        "recomendacion": "Mantenimiento preventivo regular (filtros, presión de llantas) para conservar la eficiencia."
    },

    {
        "nombre": "Regla 5 - Alta relación potencia/peso",
        "condiciones": ["potencia_alta"],
        "conclusion": "Perfil de alto rendimiento (mayor consumo esperado)",
        "recomendacion": "Esperar un consumo por encima del estimado en conducción deportiva."
    },

    {
        "nombre": "Regla 6 - Tecnología antigua en vehículo pesado",
        "condiciones": ["tecnologia_antigua", "peso_pesado"],
        "conclusion": "Vehículo antiguo y pesado: eficiencia reducida",
        "recomendacion": "Considerar actualización tecnológica o mantenimiento reforzado por antigüedad del motor."
    },

    {
        "nombre": "Regla 7 - Tecnología moderna en vehículo ligero",
        "condiciones": ["tecnologia_moderna", "peso_ligero"],
        "conclusion": "Vehículo moderno y eficiente",
        "recomendacion": "Mantener los buenos hábitos de mantenimiento actuales."
    }
]


# ------------------------------------------------------------
# 2. OBTENER LOS HECHOS DEL VEHÍCULO
# ------------------------------------------------------------
# Los hechos representan la información conocida sobre el vehículo
# (atributos del dataset Auto MPG).

def obtener_hechos():

    print("\n======================================")
    print("\n============INTERFAZ==================")
    print("   SISTEMA EXPERTO - CONSUMO DE COMBUSTIBLE")
    print("======================================")

    cylinders = int(input("Ingrese el número de cilindros (3-8): "))
    horsepower = float(input("Ingrese la potencia en caballos de fuerza (horsepower): "))
    weight = float(input("Ingrese el peso del vehículo en libras (weight): "))
    model_year = int(input("Ingrese el año de modelo (70-82): "))

    # --------------------------------------------------------
    # Convertimos los datos en HECHOS.
    # --------------------------------------------------------

    hechos = set()

    if weight > 4000:
        hechos.add("peso_pesado")
    elif weight > 2800:
        hechos.add("peso_medio")
    else:
        hechos.add("peso_ligero")

    if cylinders >= 8:
        hechos.add("motor_grande")
    elif cylinders in (5, 6):
        hechos.add("motor_mediano")
    else:
        hechos.add("motor_pequeno")

    relacion_potencia_peso = horsepower / weight
    if relacion_potencia_peso > 0.045:
        hechos.add("potencia_alta")
    else:
        hechos.add("potencia_normal")

    if model_year >= 80:
        hechos.add("tecnologia_moderna")
    else:
        hechos.add("tecnologia_antigua")

    return hechos


# ------------------------------------------------------------
# 3. MOTOR DE INFERENCIA
# ------------------------------------------------------------

def motor_inferencia(hechos):
    """
    Compara los hechos conocidos con las condiciones
    de cada regla.

    Si todas las condiciones de una regla están presentes,
    la regla se activa y genera una conclusión.
    """

    resultados = []

    print("\n======================================")
    print("        MOTOR DE INFERENCIA")
    print("======================================")

    print("\nHechos detectados:")

    for hecho in hechos:
        print("  •", hecho)

    print("\nAnalizando reglas...\n")

    for regla in reglas:

        # ----------------------------------------------------
        # Verificamos si TODAS las condiciones de la regla
        # están presentes en los hechos.
        # ----------------------------------------------------

        if all(condicion in hechos
               for condicion in regla["condiciones"]):

            print("✓ Regla activada:",
                  regla["nombre"])

            resultados.append(regla)

    return resultados


# ------------------------------------------------------------
# 4. MOSTRAR CONCLUSIONES
# ------------------------------------------------------------

def mostrar_resultados(resultados):

    print("\n======================================")
    print("          RESULTADO DEL SISTEMA")
    print("======================================")

    if not resultados:

        print("\nNo se encontró una situación específica.")
        print("Se recomienda realizar una evaluación más detallada.")

        return

    for resultado in resultados:

        print("\nDiagnóstico:")
        print("→", resultado["conclusion"])

        print("\nRecomendación:")
        print("→", resultado["recomendacion"])


# ------------------------------------------------------------
# 5. PROGRAMA PRINCIPAL
# ------------------------------------------------------------

def main():

    # Obtener información del vehículo
    hechos = obtener_hechos()

    # Ejecutar el razonamiento
    resultados = motor_inferencia(hechos)

    # Mostrar las conclusiones
    mostrar_resultados(resultados)


if __name__ == "__main__":
    main()
