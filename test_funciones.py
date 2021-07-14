import pytest
import pandas as pd
import numpy as np
import funciones
from funciones import calc_ahorroanual
from funciones import gastos_anual
from funciones import media_gastoanual
from funciones import mes_mayorahorro
from funciones import mes_mayorgasto

def test_ahorroanual():
    testdf = pd.DataFrame()
    numerosa = [-2,-4]
    numerosb = [2,-8]
    testdf['Columna1'] = numerosa
    testdf['Columna2'] = numerosb
    x = testdf
    resultado = 2.0
    assert resultado == calc_ahorroanual(x)

def test_gastoanual():
    testdf = pd.DataFrame()
    numerosa = [-2,-4]
    numerosb = [2,-8]
    testdf['Columna1'] = numerosa
    testdf['Columna2'] = numerosb
    x = testdf
    x = testdf
    resultado = -14.0
    assert resultado == gastos_anual(x)

def test_media_gastoanual():
    testdf = pd.DataFrame()
    numerosa = [-2,-4]
    numerosb = [6,-8]
    testdf['Columna1'] = numerosa
    testdf['Columna2'] = numerosb
    x = testdf
    resultado = -7.0
    assert resultado == media_gastoanual(x)

def test_mesmayorahorro():
    mesdf = pd.DataFrame(columns = ['Enero','Febrero','Marzo'])
    mesdf['Enero'] = [1,2]
    mesdf['Febrero'] = [3,4]
    mesdf['Marzo'] = [5,6]
    dftotalesmes = pd.DataFrame()
    dftotalesmes["Totales positivos"] = mesdf[mesdf>0].sum(axis = 0)
    y = dftotalesmes["Totales positivos"]
    resultado = 11.0
    assert resultado == mes_mayorahorro(y)

def test_mesmayorgasto():
    mesdf = pd.DataFrame(columns = ['Enero','Febrero','Marzo'])
    mesdf['Enero'] = [-2,-1]
    mesdf['Febrero'] = [3,4]
    mesdf['Marzo'] = [5,6]
    dftotalesmes = pd.DataFrame()
    dftotalesmes["Totales negativos"] = mesdf[mesdf<0].sum(axis = 0)
    dftotalesmes["Totales positivos"] = mesdf[mesdf>0].sum(axis = 0)
    z = dftotalesmes["Totales negativos"]
    resultado = -3.0
    assert resultado == mes_mayorgasto(z)
