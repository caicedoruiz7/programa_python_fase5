matriz = [
    ["Juan", 45, 50, 30, 60, 40],
    ["María", 55, 45, 40, 50, 35], 
    ["Pedro", 60, 55, 45, 65, 40],
    ["Ana", 40, 45, 35, 50, 30]]

umbral_horas = 40

def analizar_recurso(fila):
    nombre = fila[0]
    horas = fila[1:]
    total_horas = sum(horas)   
    
    if total_horas > umbral_horas:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion

print("=" * 55)
print(f"{'REPORTE SEMANAL DE HORAS TRABAJADAS':^55}")
print("=" * 55)
print(f"{'Recurso':<20} {'Total Horas':>10}   {'Clasificación'}")
print("-" * 55)

for fila in matriz:
    nombre, total, clasificacion = analizar_recurso(fila)
    print(f"{nombre:<20} {total:>10} horas   {clasificacion}")
print("=" * 55)