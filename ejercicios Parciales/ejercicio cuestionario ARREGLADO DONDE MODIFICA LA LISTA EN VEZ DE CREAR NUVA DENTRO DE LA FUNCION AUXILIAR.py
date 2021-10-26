##    Se tienen 2 listas con los ratings de 2 canales de televisión, medidos hora por hora arrancando desde las 0 horas;
##    y 3 listas vacías.

##  Se pide definir la función clasifRatings(canA, canB, mayorA, igual, mayorB) que reciba estas cinco listas,
##  MODIFICANDO las tres últimas listas, de la siguiente manera:

##  En la tercera lista, se deben incluir los horarios donde el canal A superó al canal B.
##  En la cuarta lista, se deben incluir los horarios donde el canal A y el canal B tuvieron el mismo rating.
##  En la quinta lista, se deben incluir los horarios donde el canal B superó al canal A.

##  Deben quedar modificadas:

##  mayorA = [2, 3, 10, 14, 21]

##  igual = [1, 5, 11, 17]

##mayor  B= [0, 4, 6, 7, 8, 9, 12, 13, 15, 16, 18, 19, 20, 22, 23]

CanalA = [ 15, 9 , 3 , 3 , 1.2 , 1 , 4.5 , 5 , 5.2 , 5 , 6.5 , 7.4 , 7.2 , 8 , 11 , 10 , 18 , 20 , 23 , 25 , 28.1 , 28 , 25 , 23 ]
CanalB = [ 16 , 9 , 1 , 2 , 1.8 , 1 , 5.5 , 6 , 7.2 , 6 , 5.5 , 7.4 , 7.9 , 9 , 10 , 11 , 19 , 20 , 24 , 29 , 28.8 , 27 , 26 , 25 ]
mayora=[]
igual=[]
mayorb=[]

#def clasifRatings(canA, canB, mayorA, igual, mayorB):

def mayorA (CanalA,CanalB,mayora):
    for i in range (0,24):
        if CanalA[i] > CanalB[i]:
            mayora.append(i)
    return mayora

##print(mayora)
##print(mayorA(CanalA,CanalB,mayora))
##print(mayora)

#print(mayorA(CanalA,CanalB))

def horarioMismoRating (CanalA,CanalB,igual):
    for i in range (0,24):
        if CanalA[i] == CanalB[i]:
            igual.append(i)
    return igual

##print(igual)
##print(horarioMismoRating(CanalA,CanalB,igual))
##print(igual)

#print(horarioMismoRating(CanalA,CanalB))


def mayorB (CanalA,CanalB,mayorb):
    for i in range (0,24):
        if CanalA[i] < CanalB[i]:
            mayorb.append(i)
    return mayorb

##print(mayorb)
##print(mayorB(CanalA,CanalB,mayorb))
##print(mayorb)
###print(mayorB(CanalA,CanalB))


def clasifRatings(CanalA, CanalB, mayora, igual, mayorb):
    mayora=mayorA (CanalA,CanalB,mayora)
    mayorb=mayorB (CanalA,CanalB,mayorb)
    igual=horarioMismoRating (CanalA,CanalB,igual)
    return (mayora, mayorb, igual)

print(mayora)
print(mayorb)
print(igual)

a=(clasifRatings(CanalA, CanalB, mayora, igual, mayorb))
for i in a:
    print (i)

print(mayora)
print(mayorb)
print(igual)




