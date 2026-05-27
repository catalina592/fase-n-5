# berta catalina murcia
#ingenieria de sistemas
#fase 5 examen final
# fundamentos de programacion
matriz_horas = [
    ["Persona 1", 8, 9, 8, 7, 9],
    ["Persona 2", 7, 7, 7, 7, 7],
    ["Persona 3", 10, 9, 8, 10, 9],
    ["Persona 4", 8, 8, 7, 8, 8]
]

def calcular_y_clasificar(matriz, umbral_estandar=40):
    resultados_procesados = []
    for registro in matriz:
        nombre = registro[0]
        horas_por_dia = registro[1:]
        total_semanal = sum(horas_por_dia)
        if total_semanal > umbral_estandar:
            clasificacion = "Sobretiempo"
        else:
            clasificacion = "Horario Estándar o inferior"
        resultados_procesados.append([nombre, total_semanal, clasificacion])
    return resultados_procesados

resultados_finales = calcular_y_clasificar(matriz_horas)

print("=" * 55)
print("RESUMEN SEMANAL DE HORAS TRABAJADAS POR RECURSO")
print("=" * 55)
print(f"{'Recurso':<12} | {'Total Horas':<12} | {'Clasificación'}")
print("-" * 55)

for dato in resultados_finales:
    print(f"{dato[0]:<12} | {dato[1]:<12} | {dato[2]}")

print("=" * 55)