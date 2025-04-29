import pandas as pd
import numpy as np
 
datos = {'Nombre': ['Leonardo', 'Reiner', 'Alex'],
         'Materias': ['Lenguaje', 'Historia', 'Matemática'],
         'Calificaciones': ['12', '20', '17'],
         'Deportes': ['Natación', 'Tenis', 'Voley']
         }

df = pd.DataFrame(datos)
print(df)