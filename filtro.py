import pandas as pd
import os
import math
from CosasRut import CosasRut

def dfList(list):
    fList = []
    for i in list:
        if i.endswith(".xlsx"):
            fList.append(pd.read_excel('Files/'+i))
    return fList

def traducir(txt):
    dictio = {
        'dmt2':'Diabetes tipo 2',
        'hta,dm2':'Hipertensión y diabetes tipo 2',
        'dm, hta':'Hipertensión y diabetes',
        'dm,hta,dlp':'Hipertensión, diabetes y dislipidemia',
        'No aplica':'No aplica',
        'hta ':'Hipertensión',
        'no':'No aplica',
        'ca,dm':'Cáncer',
        'hta, resistencia a la insulina':'Hipertensión y resistencia a la insulina',
        'dm':'Diabetes',
        'ca':'Cáncer',
        'dm2,ca':'Diabetes tipo 2 y cáncer',
        'hta':'Hipertensión',
        'resistencia a la insulina':'Resistencia a la insulina',
        'hta,dm':'Hipertensión y diabetes',
        'dm,hta':'Hipertensión y diabetes',
        'hermana, mama hipotiroidismo y abuela DM':'Hipotiroidismo y diabetes',
        'madre, padre HTA y DMT2':'Hipertensión y diabetes tipo 2',
        'No':'No aplica',
        'abuela DM':'Diabetes',
        'abuelo DM':'Diabetes',
        'mama hipotiroidismo y abuela HTA':'Hipotiroidismo e hipertensión',
        'abuelo HTA':'Hipertensión',
        'HTA DM':'Hipertensión y diabetes',
        'padre,madre HTA':'Hipertensión',
        'mama DM abuelo DM':'Diabetes',
        'diabetes, displemia ':'Diabetes y displemia',
        'hpertension':'Hipertensión',
        'hipertension,dislipidemia':'Hipertensión y displemia',
        'hipertension,diabetes':'Hipertensión y diabetes',
        'hipertencsion':'Hipertensión',
        'hipertension':'Hipertensión',
        'Hipertensión Padre y madre':'Hipertensión',
        ' Abuelo Diabetes':'Diabetes',
        'paterna, hipertension':'Hipertensión',
        'Hipertension Abuelo':'Hipertensión',
        'papá Diabetes, Hipertension':'Hipertensión y diabetes',
        'abuelos, Diabetes, Hipertension':'Hipertensión y diabetes',
        'mamá, Hipertension':'Hipertensión',
        'mamá Diabetes, papá Hipertension':'Hipertensión y diabetes',
        'padre diabetes, madre hipertension y cancer':'Hipertensión, diabetes y cáncer',
        'papá Hipertension, abuelo paterno Diabetes':'Hipertensión y diabetes',
        'dm,hta,acu':'Hipertensión, diabetes e ACCU',
        'hma(+) dm(-)':'Diabetes y hematuria',
        'dm,tha,ob':'Diabetes, hiperactividad y obesidad',
        'hipotiroidismo,dm,tha':'Diabetes, hiperactividad e Hipotiroidismo',
        'hta,dm,dislipidemia':'Hipertensión, diabetes y Dislipidemia',
        'atc,cuc,trigliceridos':'Antidepresivos, colitis ulcerosa y Trigliceridos',
        'res insulina':'Resistencia a la insulina',
        'Abuela HTA':'Hipertensión',
        'Madre HTA':'Hipertensión',
        'Madre y Padre DMT2':'Diabetes tipo 2',
        'Abuela Diabetes':'Diabetes',
        'HTA padres, DMT2 Madre':'Hipertensión y diabetes tipo 2',
        'DM padre, madre HTA':'Hipertensión y diabetes',
        'Padre DM':'Diabetes',
        'HTA':'Hipertensión',
        'Hija DM, Abuela DM':'Diabetes',
        'Mama DM':'Diabetes',
        'hermano HTA':'Hipertensión',
        'HTA, DM abuelo ':'Hipertensión y diabetes',
        'papa y mama HTA':'Hipertensión',
        ' HTA/DM':'Hipertensión y diabetes',
        'Abuela HTA, Papa HTA':'Hipertensión',
        'Mama= Resistencia a la insulinda- HTA, Abuela= DM':'Hipertensión, diabetes y resistencia a la insulina',
        'Hipertiroidismo':'Hipertiroidismo',
        'Abuelos= HTA Y DM':'Hipertensión y diabetes',
        'MAMA= DM/Sarcoidosis':'Diabetes y Sarcoidosis',
        'Abuelos y mama= HTA Y DM':'Hipertensión y diabetes',
        'PADRES= HTA Y DM':'Hipertensión y diabetes',
        'Abuela DM':'Diabetes',
        'PAPA= DM2-HTA':'Hipertensión y diabetes tipo 2',
        'DM':'Diabetes',
        'HTA,DM':'Hipertensión y diabetes',
        ' HTA,DM POEPO':'Hipertensión y diabetes',
        'Abuelo HTA, Abuela DM2':'Hipertensión y diabetes tipo 2',
        'HTA Papá':'Hipertensión',
        'Papá HTA':'Hipertensión',
        '(Abuelo - Madre) Cancer':'Cáncer'
    }
    return dictio[txt]

def SiNo(op):
    ops = {'si':'Si','no':'No',
           'Si':'Si','No':'No'}
    return ops[op]

files = os.listdir('Files')


dataFrames = dfList(files)

ruts = []

columnas = dataFrames[0].columns

datosDF = {}
for i in range(len(columnas)):
    datosDF.update({columnas[i]:[]})


for i in range(len(dataFrames)):
    for j in range(len(dataFrames[i]['Rut'])):
        limpio = CosasRut.limpiaRut(dataFrames[i]['Rut'][j])
        if not limpio in ruts and CosasRut.validaRut(limpio):
            for k in columnas:
                if k != 'Rut':
                    if (k != 'Mujer >= 88' and k != 'hombre >=102'):
                        if k == 'Antecedentes familiar':
                            if isinstance(dataFrames[i][k][j], float) and math.isnan(dataFrames[i][k][j]):
                                datosDF[k].append('No aplica')
                            else:
                                datosDF[k].append(traducir(dataFrames[i][k][j]))
                        else:
                            if isinstance(dataFrames[i][k][j], float) and math.isnan(dataFrames[i][k][j]):
                                datosDF[k].append('No aplica')
                            else:
                                datosDF[k].append(dataFrames[i][k][j])
                    else:
                        if isinstance(dataFrames[i][k][j], float) and math.isnan(dataFrames[i][k][j]):
                            datosDF[k].append('No aplica')
                        else:
                            datosDF[k].append(SiNo(dataFrames[i][k][j]))
                else:
                    datosDF[k].append(limpio)
        elif not CosasRut.validaRut(limpio):
            for c in dataFrames[i].columns:
                print(dataFrames[i]['Rut'][j])
                print(dataFrames[i][c][j],'\n')

#for i in datosDF:
#    print(i)
    #for j in datosDF[i]:
        #print(j)
    """
    if k == 'Antecedentes familiar':
    cont = input('continuar s/n: ')
    if cont != 's':
        break
    else:
        print('\n')
    """
print('\nFIN\n')
DF = pd.DataFrame(datosDF,columns = columnas)

#print(DF)
#DF.to_excel('dataFrame.xlsx')

