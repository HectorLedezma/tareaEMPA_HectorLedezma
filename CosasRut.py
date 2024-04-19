import random as rn
import math

class CosasRut:
    def __init__(self):
        pass
    
    def validaRut(rut):#10.200.300-6
        
        try:
            rutschar = ''
            caracteres="0123456789K"
            for x in rut:
                if x in caracteres:
                    rutschar += x
                elif x == 'k':
                    rutschar += 'K'

            rutsindigito=rutschar[:len(rutschar)-1]#10200300
            rutinvertido=rutsindigito[::-1]#00300201
            multi=2
            sum=0
            for i in range(0,len(rutinvertido)):
                if multi > 7:
                    multi=2
                sum+=int(rutinvertido[i])*multi
                multi+=1

            dv=11-(sum%11)
            dvu=rut[-1:]
            ##print('dvu:',dvu)
            if dv==11:
                dv=0
            if dv==10:
                dv="K"
            if str(dv)==dvu:
                return True
            else:
                return False
        except:
            return False

    def creaRut(self, g1=None,g2=None,g3=None,div=None):
        casos = [g1,g2,g3,div]
        bin = 0
        for i in range(len(casos)):
            if casos[i] != None:
                bin += int(math.pow(2,i))
        
        rutDefinitivo = ''
        while True:
            if bin == 0 or bin == 8:    #0000  0001
                rutInt = rn.randint(8000000,21000000)
                
            elif bin == 1 or bin == 9:  #1000  1001
                rutInt = rn.randint(g1*1000000,(g1+1)*1000000)
                
            elif bin == 2 or bin == 10: #0100  0101
                rutInt = rn.randint(8,21)*1000000+((g2*1000)+rn.randint(0,1000))# (8000000 - 21000000) + 600000 + (0-1000)
                
            elif bin == 3 or bin == 11: #1100  1101
                rutInt = rn.randint((g1*1000000)+(g2*1000),((g1)*1000000)+((g2+1)*1000))#20.600.000 - 20.700.000
                
            elif bin == 4 or bin == 12: #0010  0011
                rutInt = (rn.randint(8000,21000)*1000)+g3
                
            elif bin == 5 or bin == 13: #1010  1011
                rutInt = (rn.randint((g1*1000),((g1+1)*1000))*1000)+(g3)#[20.000.000-21.000.000]
                
            elif bin == 6 or bin == 14: #0110  0111
                rutInt = rn.randint(8,21)*1000000+((g2*1000)+g3)
            
            elif bin == 7 or bin == 15: #1110: #1111
                rutInt = (g1*1000000)+(g2*1000)+g3
            
            rutStr = str(rutInt)
            #9312438
            #8342139
            rutStri = rutStr[::-1]
            
            rutPts = ''
            for i in range(len(rutStri)):
                if i == 2 or i == 5:
                   rutPts = rutPts + rutStri[i] + '.'
                else:
                    rutPts = rutPts + rutStri[i]
            
            rutPtsi = rutPts[::-1]
            digver = ''
            if bin >= 8:
                if div == 'k':
                    div = 'K'
                digver = str(div)
            else:
                digver = rn.choice(["0","1","2","3","4","5","6","7","8","9","K"])
            rut = rutPtsi+"-"+digver
            
            if self.validaRut(rut):
                rutDefinitivo = rut
                break
        return rutDefinitivo

    def corrigeRut(bueno,malo,similitud):
        texto1 = bueno
        texto2 = malo
        exactitud = 0.0 #inicia con 0% de exactitud
        cont = 0 #de momento hay 0 caracteres idénticos
        #print('Bueno',bueno)
        #print('Malo',malo)
        #print(texto2)
        EsNaN = texto2 == None
        #print(EsNaN)
        if not EsNaN:
            #print('listo para comparar')
            for i in range(min(len(texto1),len(texto2))): #se recorrerán los caracteres del el rut mas corto 
                if(texto1[i] == texto2[i]):#se comparan y se cuentan los caracteres idénticos
                    cont += 1
            exactitud = round((cont/max(len(texto1),len(texto2)))*100,1)#se calcula el porcentaje de exactitud
            if exactitud >= similitud:
                #print(malo,'-->',bueno,exactitud,exactitud >= similitud)
                return True#si la exactitud es igual o mayor a lo esperado retorna 
            else:
                return False
        else:
            return False
    
    def limpiaRut(rut):
        newRut = ''
        try:
            #print(rut)
            
            caracteres="0123456789K"
            rutschar = ''
            for x in rut:
                if x in caracteres:
                    rutschar += x
                elif x=='k':
                    rutschar += 'K'
            #print(rutschar)
            
            dv = rutschar[len(rutschar)-1] #     8
            rutsdv = rutschar[:len(rutschar)-1]
            #print(rutsdv)
            
            rutinvertido=rutsdv[::-1]
            #print(rutinvertido)
            
            rutcpt = ''
            for i in range(len(rutinvertido)):
                if i == 2 or i == 5:
                    rutcpt = rutcpt + rutinvertido[i]+'.'
                else:
                    rutcpt += rutinvertido[i]
            #print(rutcpt)
            
            rutcpti = rutcpt[::-1]
            #print(rutcpti)
            
            newRut = rutcpti+'-'+dv
            #print(newRut)
        except:
            newRut = None     
        return newRut
   