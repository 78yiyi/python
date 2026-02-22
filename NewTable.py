import pandas as pd
import io

# Cargar los datasets originales
df_pioneros = pd.read_csv('Misión 3_ DashBoard - Profes.xlsx - 1 - Pioneros.csv')
df_evolucion = pd.read_csv('Misión 3_ DashBoard - Profes.xlsx - 2 - Evolución.csv')
df_matriz = pd.read_csv('Misión 3_ DashBoard - Profes.xlsx - 3 - Matriz.csv')

# 1. Etiquetar el origen de los datos
df_pioneros['FUENTE_TABLA'] = 'Pioneros (Historia)'
df_evolucion['FUENTE_TABLA'] = 'Evolución (Web 1.0-3.0)'
df_matriz['FUENTE_TABLA'] = 'Matriz (Apps Actuales)'

# 2. Normalizar fechas para que sean texto (y evitar conflictos de tipo de dato)
df_pioneros['Año'] = df_pioneros['Año'].astype(str)
df_evolucion['Década'] = df_evolucion['Década'].astype(str)

# 3. Crear Columnas Maestras (Mapeo de campos)

# --- PIONEROS ---
df_pioneros['MASTER_Nombre'] = df_pioneros['Hito Tecnológico']
df_pioneros['MASTER_Fecha'] = df_pioneros['Año']
df_pioneros['MASTER_Categoria'] = df_pioneros['Tipo']
df_pioneros['MASTER_Ubicacion'] = df_pioneros['País']
df_pioneros['MASTER_Entidad'] = df_pioneros['Figura/Componente']

# --- EVOLUCIÓN ---
df_evolucion['MASTER_Nombre'] = df_evolucion['Herramienta Ejemplo']
df_evolucion['MASTER_Fecha'] = df_evolucion['Década']
df_evolucion['MASTER_Categoria'] = df_evolucion['Concepto Clave']
df_evolucion['MASTER_Ubicacion'] = None # No tiene país específico en origen, pero se podría inferir
df_evolucion['MASTER_Entidad'] = df_evolucion['Empresa Líder']

# --- MATRIZ ---
df_matriz['MASTER_Nombre'] = df_matriz['Plataforma']
df_matriz['MASTER_Fecha'] = 'Actualidad' # Valor por defecto para las apps actuales
df_matriz['MASTER_Categoria'] = df_matriz['Categoría']
df_matriz['MASTER_Ubicacion'] = df_matriz['Sede']
df_matriz['MASTER_Entidad'] = None # No tiene columna de CEO/Fundador específica mapeada aqui

# 4. Concatenar (Fundir) las tablas
df_final = pd.concat([df_pioneros, df_evolucion, df_matriz], axis=0, ignore_index=True)

# Reordenar columnas para poner las MASTER al principio (opcional, por estética)
cols = list(df_final.columns)
master_cols = ['FUENTE_TABLA', 'MASTER_Nombre', 'MASTER_Fecha', 'MASTER_Categoria', 'MASTER_Ubicacion', 'MASTER_Entidad']
# Remover las master de la lista original para no duplicar
cols = [c for c in cols if c not in master_cols]
# Nueva lista ordenada
final_order = master_cols + cols
df_final = df_final[final_order]

# Guardar
df_final.to_csv('Tabla_Maestra_Unificada.csv', index=False)
print("Archivo creado con éxito.")