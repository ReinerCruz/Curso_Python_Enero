import pandas as pd
import numpy as np
 
# %%
datos = {'Nombre': ['Leonardo', 'Reiner', 'Alex'],
         'Materias': ['Lenguaje', 'Historia', 'Matemática'],
         'Calificaciones': ['12', '20', '17'],
         'Deportes': ['Natación', 'Tenis', 'Voley']
         }

df = pd.DataFrame(datos)
print(df)
print('\n'*4)

# %%
# Datos no válidos

datos2 = {'Nombre': ['Leonardo', 'Reiner', 'N/A'],
         'Materias': ['Lenguaje', 'Historia', 'Matemática'],
         'Calificaciones': ['12', np.nan, '17'],
         'Deportes': ['Natación', 'N/A', 'Voley']
         }


df2 = pd.DataFrame(datos2)
print(df2)
print('\n'*1)
print(df2.info())

# %%
# Estadísticas básicas

df2.describe()
nuevo = pd.DataFrame(datos2)
nuevo = nuevo.replace(np.nan, 'O')
print(nuevo)

# %% Eliminar registros por columnas

columna = df2[df2['Nombre'] != 'N/A']
print(columna)
print('\n'*1)

columna2 = df2[~df2['Nombre'].isin(['Reiner', 'Leonardo'])] #Eliminar registros de varias filas de una vez
print(columna2 )

# %% Convertir los números a enteros. Recuerda que Calificaciones está como string

df['Calificaciones'] = df.Calificaciones.astype(int)
print(df.describe())

# %% Estadísticas individuales

print('El promedio de las calificaciones es', df['Calificaciones'].mean())
