equipo = [
    ["Juan",  9,  8, 10,  7,  9],   
    ["María", 8,  8,  8,  8,  8],   
    ["Pedro", 10, 9, 10,  9,  8],   
    ["Ana",   6,  7,  8,  6,  7],   
]

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

for fila in equipo:
    nombre, total, clasificacion = analizar_recurso(fila)
    print(f"{nombre:<20} {total:>10} horas   {clasificacion}")
print("=" * 55)