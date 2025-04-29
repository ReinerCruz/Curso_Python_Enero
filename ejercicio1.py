import pandas as pd
import numpy as np
 
datos = {'Nombre': ['Leonardo', 'Reiner', 'Alex'],
         'Materias': ['Lenguaje', 'Historia', 'Matemática'],
         'Calificaciones': ['12', '20', '17'],
         'Deportes': ['Natación', 'Tenis', 'Voley']
         }

df = pd.DataFrame(datos)
print(df)
print('\n'*4)

# Datos no válidos

datos2 = {'Nombre': ['Leonardo', 'Reiner', 'Alex'],
         'Materias': ['Lenguaje', 'Historia', 'Matemática'],
         'Calificaciones': ['12', np.nan, '17'],
         'Deportes': ['Natación', 'N/A', 'Voley']
         }


df2 = pd.DataFrame(datos2)
print(df2)
print('\n'*1)
print(df2.info())

