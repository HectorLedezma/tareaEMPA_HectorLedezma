import pandas as pd
import os

def dfList(list):
    fList = []
    for i in list:
        fList.append(pd.read_excel('Files/'+i))
    return fList


files = os.listdir('Files')

dataframes = dfList(files)

ruts = []

for i in range(len(files)):
    print('Archivo:',files[i])
    print(dataframes[i])
    print(dataframes[i].head())
    #if 'Rut' in dataframes[i].head():
    #    ruts.insert(dataframes[i]['Ruts'])
    cont = input('continuar s/n: ')
    if cont != 's':
        break
    else:
        print('\n')
print('\nFIN\n')

print(ruts)
