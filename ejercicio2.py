# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:52:58 2025

@author: Reiner Gaga
"""
# %% Establecemos el directorio

import os
os.chdir(r"C:\Users\Mi Equipo\Curso_Python_Enero")

# %% Leemos la tabla de información

import pandas as pd
import numpy as np

df = pd.read_csv('ATP.csv', encoding = 'latin-1')
print(df.head())

