import random as rn

class CosasRut:
    def __init__(self):
        pass
    
    def validaRut(rut):#10.200.300-6
        caracteres=".-"
        for x in range(len(caracteres)):
            rut=rut.replace(caracteres[x],"")#102003006

        rutsindigito=rut[:len(rut)-1]#10200300
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

    def creaRut(self):
        rutDefinitivo = ''
        while True:
            rutInt = rn.randint(8000000,21000000)
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
            rut = rutPtsi+"-"+rn.choice(["0","1","2","3","4","5","6","7","8","9","k"])
        
            if self.validaRut(rut):
                rutDefinitivo = rut
                break
        return rutDefinitivo

    def limpiaRut(rut):
        newRut = ''
        try:
            #print(rut)
            
            caracteres="0123456789k"
            rutschar = ''
            for x in rut:
                if x in caracteres:
                    rutschar += x
                elif x=='K':
                    rutschar += 'k'
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
   