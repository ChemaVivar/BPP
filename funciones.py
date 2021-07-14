import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


try:
    df = pd.read_csv('finanzas2020.csv', sep='\t')

except IOError:
    print("No se encuentra o imposible leer el archivo")
else:
    print("Archivo leído correctamente")
    print()

def comprobarcolumnas():
    if len(df.columns) < 12:
        Raise(ValueError, "El número de columnas es menor que 12, faltan datos")
    else:
        print("Cantidad de columnas correcta")
        print()
comprobarcolumnas()

def limpiar_valoresdf():
    try:
        df['Enero'] = df['Enero'].str.replace('\'', '')
        df['Enero'] = df['Enero'].astype(int)
        df['Julio'] = df['Julio'].str.replace('\'', '')
        df['Julio'] = df['Julio'].astype(int)
        df['Noviembre'] = df['Noviembre'].str.replace('\'', '')
        df['Noviembre'] = df['Noviembre'].astype(int)

    except:
        print("No pudieron convertirse todas las columnas")

limpiar_valoresdf()

lista = df.transpose().to_numpy().tolist()

lista_en = df['Enero'].to_numpy().tolist()
lista_feb = df['Febrero'].to_numpy().tolist()
lista_mar = df['Marzo'].to_numpy().tolist()
lista_ab = df['Abril'].to_numpy().tolist()
lista_may = df['Mayo'].to_numpy().tolist()
lista_jun = df['Junio'].to_numpy().tolist()
lista_jul = df['Julio'].to_numpy().tolist()
lista_ag = df['Agosto'].to_numpy().tolist()
lista_sep = df['Septiembre'].to_numpy().tolist()
lista_oct = df['Octubre'].to_numpy().tolist()
lista_nov = df['Noviembre'].to_numpy().tolist()
lista_dic = df['Diciembre'].to_numpy().tolist()

lista12 = [[lista_en], [lista_feb], [lista_mar], [lista_ab],[lista_may],
            [lista_jun],[lista_jul], [lista_ag], [lista_sep], [lista_oct],
            [lista_nov], [lista_dic]]

processed_data = []
for i in range(0,len(lista12)):
    aux_lista = []
    for j in lista[i]:
        try:
            aux = int(j)
            aux_lista.append(aux)
        except:
            aux_lista.append(0)
            print("no puedo convertir el valor", j)
    processed_data.append(aux_lista)
print()
lista_meses = processed_data

newdf = pd.DataFrame(lista_meses[0], columns = ['Enero'])
newdf['Febrero'] = pd.DataFrame(lista_meses[1], columns = ['Febrero'])
newdf['Marzo'] = pd.DataFrame(lista_meses[2], columns = ['Marzo'])
newdf['Abril'] = pd.DataFrame(lista_meses[3], columns = ['Abril'])
newdf['Mayo'] = pd.DataFrame(lista_meses[4], columns = ['Mayo'])
newdf['Junio'] = pd.DataFrame(lista_meses[5], columns = ['Junio'])
newdf['Julio'] = pd.DataFrame(lista_meses[6], columns = ['Abril'])
newdf['Agosto'] = pd.DataFrame(lista_meses[7], columns = ['Agosto'])
newdf['Septiembre'] = pd.DataFrame(lista_meses[8], columns = ['Septiembre'])
newdf['Octubre'] = pd.DataFrame(lista_meses[9], columns = ['Octubre'])
newdf['Noviembre'] = pd.DataFrame(lista_meses[10], columns = ['Noviembre'])
newdf['Diciembre'] = pd.DataFrame(lista_meses[11], columns = ['Diciembre'])

dftotalesmes = pd.DataFrame()
dftotalesmes["Totales positivos"] = newdf[newdf>0].sum(axis = 0)
dftotalesmes["Totales negativos"] = newdf[newdf<0].sum(axis = 0)


print()
print()


def calc_ahorroanual(x):
    ahorromensual = x[x>0].sum()
    ahorrosanual = (x[x>0].sum()).sum()
    print(f'Los ingresos totales anuales son {ahorrosanual}')
    return (x[x>0].sum()).sum()
x = newdf
calc_ahorroanual(x)

def gastos_anual(x):

    gastosmes = x[x<0].sum()
    gastoanual = (x[x<0].sum()).sum()
    print(f'Los gastos totales anuales son de {gastoanual}')
    return (x[x<0].sum()).sum()

x = newdf
gastos_anual(x)

def media_gastoanual(x):

    media_gastoanual = (x[x<0].sum()).mean()
    print(f'La media de gasto anual es de {media_gastoanual}')
    return (x[x<0].sum()).mean()

x = newdf
media_gastoanual(x)

def mes_mayorahorro(y):
    mesmayoringreso = y.max()
    nombremesmayor = y.idxmax()
    print(f'El mes de mayor ahorro es {nombremesmayor}, con la cifra de {mesmayoringreso}')
    return y.max()

y=dftotalesmes['Totales positivos']
mes_mayorahorro(y)

def mes_mayorgasto(z):
    mes_mayorgasto = z.min()
    nombremesmenor = z.idxmin()
    print(f'El mes de mayor gasto es {nombremesmenor}, con la cifra de {mes_mayorgasto}')
    return z.min()
z=dftotalesmes['Totales negativos']
mes_mayorgasto(z)
