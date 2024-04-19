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
        'dm ':'Diabetes',
        'alergia':'Alergia',
        'alergia,':'Alergia',
        'Asma y alergia':'Asma y alergia',
        'depresión,ansiedad':'Depresión y Ansiedad',
        'Abuelo, diabetes/hipertension':'Hipertensión y diabetes',
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
        'madre diabetes, hipertension':'Hipertensión y diabetes',
        'Madre HTA':'Hipertensión',
        'madre HTA':'Hipertensión',
        'PADRES= HTA':'Hipertensión',
        'Papa y Mama= HTA':'Hipertensión',
        'Madre y Padre DMT2':'Diabetes tipo 2',
        'MADRE= DM2':'Diabetes tipo 2',
        'Abuela Diabetes':'Diabetes',
        'HTA padres, DMT2 Madre':'Hipertensión y diabetes tipo 2',
        'HTA padre, DMT2 abuelo':'Hipertensión y diabetes tipo 2',
        'DM padre, madre HTA':'Hipertensión y diabetes',
        'hta,ca':'Hipertensión y cancer',
        'Insuf renal papa, HTA DMTA mama':'Hipertensión, insuficiencia renal y degeneración macular',
        'Padre DM':'Diabetes',
        'DM Padres':'Diabetes',
        'HTA papa, fibromialgia mama':'Hipertensión y fibromialgia',
        'HTA':'Hipertensión',
        'madre Hipertension':'Hipertensión',
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
        '(Abuelo - Madre) Cancer':'Cáncer',
        'Hipertensión y diabetes tipo 2':'Hipertensión y diabetes tipo 2',
        'No aplica':'No aplica',
        'Hipertensión y diabetes':'Hipertensión y diabetes',
        'Hipertensión':'Hipertensión',
        'Diabetes':'Diabetes',
        'asma cronico':'Asma crónico', 
        'htd':'Hipotiroidismo', 
        'hipotireoidismo':'Hipotiroidismo', 
        'resistencia insulina':'Resistencia insulina', 
        'osteoporosis, iteroctomia parcial':'Osteoporosis e iteroctomia parcial', 
        'Ninguno':'No Aplica', 
        'Ansiedad':'Ansiedad', 
        'asma':'Asma', 
        'Ninguna':'No Aplica', 
        'derivacion a matrona para PAP':'Papanicolau', 
        'polineuropatia hereditaria':'Polineuropatia', 
        'ninguno':'No Aplica', 
        'cefalio cronico':'Cefalio crónico', 
        'no ':'No Aplica', 
        'Resistente a la insulina, rinitis alergica':'Resistencia insulina y Rinitis alergica', 
        'ninguna':'No Aplica', 
        'asma ':'Asma', 
        'hipotiroidismo,resistencia a la insulina':'Resistencia insulina e hipotiroidismo', 
        'gastritis,dm':'Gastritis y diabetes', 
        'dislipidemia':'Dislipidemia', 
        'Asma ':'Asma', 
        'Asma':'Asma', 
        'Dislipidemia(atorvastatina)':'Dislipidemia', 
        'Enf coronaria, taco':'Enfermedad coronaria y taco', 
        'NO':'No Aplica', 
        'resistencia a la insulina ':'Resistencia insulina', 
        'RI':'Resistencia insulina', 
        'Cancer cervicouterino':'Cancer', 
        'Diabetes Gestacional':'Diabetes', 
        'Hta':'Hipertension', 
        'Perfil PA':'Presión Arterial', 
        'Congestion pulmonar':'Congestion pulmonar'
    }
    return dictio[txt]

def SiNo(op):
    ops = {'si':'Si','no':'No',
           'Si':'Si','No':'No'}
    return ops[op]

files = os.listdir('Files')

dataFrames = dfList(files)

rutsBuenos = []
rutsMalos = []

datosDF = {}#se crea un diccionario vacio para colocar los datos del nuevo DF
for c in dataFrames[0]:
    datosDF.update({c:[]})#se le asignan las mismas columnas de los otros DF

ruts = []
        
for d in dataFrames:#se recorre la lista de DFs
    for c in d:#se recorren las columnas de los DFs
        for f in d[c]: #se recorre la fila de cada columna
            
            if c == 'Rut':#Acciones a realizar en la columna "Rut"
                rutMalos = []
                rutBueno = []
                if CosasRut.validaRut(CosasRut.limpiaRut(f)):
                    datosDF[c].append(CosasRut.limpiaRut(f))    
                else:
                    found = False
                    for r in datosDF[c]:
                        if CosasRut.corrigeRut(r,CosasRut.limpiaRut(f),75.0):
                            datosDF[c].append(r)
                            found = True
                            break
                    if not found:
                        datosDF[c].append('')
            elif c == 'Antecedentes familiar' or c == 'Antecedentes morbilidad':
                if isinstance(f,float) and math.isnan(f):
                    datosDF[c].append('No aplica')
                else:
                    datosDF[c].append(traducir(f))
            elif c != 'Fecha' and c != 'fecha':
                if (isinstance(f,float) and math.isnan(f)):
                    datosDF[c].append('No aplica')
                elif f == '-':
                    datosDF[c].append('No aplica')
                else:
                    datosDF[c].append(f)
                    

datosDF2 = {}
for c in dataFrames[0]:
    datosDF2.update({c:[]})

for c in dataFrames[0]:
    for i in range(len(datosDF['Rut'])):
        #print('¿',datosDF['Rut'][i],'Se repite? -> ',not datosDF['Rut'][i] in datosDF2['Rut'])
        if datosDF['Rut'][i] != '':
            datosDF2[c].append(datosDF[c][i])

datosDF3 = {}
for c in dataFrames[0]:
    datosDF3.update({c:[]})

rutNoRep = []



for i in range(len(datosDF2['Rut'])):
    if not datosDF2['Rut'][i] in rutNoRep:
        rutNoRep.append(datosDF2['Rut'][i])



for i in datosDF2:#llaves
    for j in range(len(rutNoRep)):
        for k in range(len(datosDF2['Rut'])):
            if datosDF2['Rut'][k] == rutNoRep[j]:
                datosDF3[i].append(datosDF2[i][k])
                break
        

#correcciones = []# se crea una lista para las correcciones de RUT


"""
limpio = CosasRut.limpiaRut(dataFrames[i]['Rut'][j])#se limpia el RUT de la fila j
        
        if CosasRut.validaRut(limpio):#si el rut limpio es valido
            
            rutsBuenos.append(dataFrames[i]['Rut'][j])#se añade a una lista de RUTs validos
            
        else:
            rutsMalos.append(dataFrames[i]['Rut'][j])#si no, se añade a una lista de RUTs no validos


for m in rutsMalos:#se recorre la lista de ruts no validos
    found = False#variable para saber si se encontró relación entre los rut a comparar
    for b in rutsBuenos:#se recorre la lista de ruts validos
        if CosasRut.corrigeRut(CosasRut.limpiaRut(b),CosasRut.limpiaRut(m),75.0):
            #si el rut no valido tiene un 75% o mas de similitud con un valido
            correcciones.append({'RutBueno':b,'RutMalo':m})#se llena la lista de correcciones
            found = True#si se encontró se cambia el valor a verdadero
            break
    if not found:#si no se encontró similitud entre los ruts a comparar
        correcciones.append({'RutBueno':None,'RutMalo':m})#se reemplazara por un valor nulo

#print(correcciones)

ruts = []
for i in range(len(dataFrames)):#recorre la lista DFs
    
    for rut in dataFrames[i]['Rut']:#se recorre la columna "Rut" del DF i
        if not CosasRut.validaRut(rut):# si el rut no es valido
            
            for cor in correcciones:#se recorre la lista de correcciones
                if cor['RutMalo'] == rut:#si el rut conicide con los no validos
                    dataFrames[i] = dataFrames[i].replace(rut,CosasRut.limpiaRut(cor['RutBueno']))
                    #es reemplazado de su DF por el valido mas parecido
                    break
                
        else:#si es valido es reemplazado de su DF por si mismo pero limpio
            dataFrames[i] = dataFrames[i].replace(rut,CosasRut.limpiaRut(rut))
    
    for j in dataFrames[i]:#recorre las columnas de cada DF
        for r in range(len(dataFrames[i][j])):#recorre las filas de cada DF
            
            #if j == 'Rut':# se centra en la columna "Rut":
            #    if dataFrames[i]['Rut'][r] == None:
            #        dataFrames[i].drop(r,axis=0,inplace=True)#se eliminan las filas que no tengan rut
            if j == 'Antecedentes familiar':
                #se centra en la columna "Antecedentes familiar"
                #print(dataFrames[i][j][r])
                if not isinstance(dataFrames[i][j][r],float):
                    dataFrames[i] = dataFrames[i].replace(dataFrames[i][j][r],traducir(dataFrames[i][j][r]))
                else:
                    dataFrames[i] = dataFrames[i].replace(dataFrames[i][j][r],'No aplica')
                
        




    
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



if k == 'Antecedentes familiar':
cont = input('continuar s/n: ')
if cont != 's':
    break
else:
    print('\n')
"""

print('\nFIN\n')

#for i in datosDF2:
#    print(i,len(datosDF2[i]))

#print(datosDF)
#for i in datosDF:
#    print(i,len(datosDF[i]))
DF = pd.DataFrame(datosDF3)
#print(DF)

DF.to_excel('dataFrame.xlsx')

