import pandas as pd
import numpy as np

# Configurar fechas para simular 3 meses de tickets
np.random.seed(42)
fechas = pd.date_range(start='2026-01-01', end='2026-03-31', freq='h')

# Crear datos aleatorios realistas para una mesa de ayuda
n = len(fechas)
df = pd.DataFrame({
    'fecha_hora': fechas,
    'dia_semana': fechas.day_name(),
    'hora': fechas.hour,
    'volumen_tickets': np.random.poisson(lam=5, size=n), # Cantidad de tickets por hora
    'tiempo_atencion_promedio': np.random.uniform(3, 15, size=n) # Minutos
})

# Guardar como archivo Excel virtual para la prueba
df.to_excel('tickets_historico.xlsx', index=False)
print("¡Archivo 'tickets_historico.xlsx' generado con éxito!")
