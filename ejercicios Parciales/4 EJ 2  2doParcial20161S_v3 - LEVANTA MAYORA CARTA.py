##  Ejercicio 2: (3 puntos)
##  Tres amigos juegan una partida de naipes donde en cada ronda los jugadores levantan una carta y pierde quien
##  tenga la carta de mayor valor. Cada carta tiene un valor dependiendo de su número (denominación) y su palo.
##  Se conocen 4 rondas: (T: Trébol, C: Corazón, P: Pica, D: Diamante)

#              Ronda 1 Ronda 2 Ronda 3 Ronda 4
#  Jugador_1     2T     10C      AD     QD
#  Jugador_2     AT     8C       2D     AC
#  Jugador_3     7T     AP       KD     10D

## Hacer el programa que muestre los puntos obtenidos por cada jugador en cada ronda y cuál pierde. Las cartas
## tienen valor por su número, siendo el As la de mayor valor y también por su palo. Se dan las listas a usar:

Deno      = [2,3,4,5,6,7,8,9,10,'j','q','k','a']
valorDeno = [2,3,4,5,6,7,8,9,10,11 ,12 , 13, 14]

palo      = ['D','P','C','T'] #Diamante, Pica, Corazón, Trébol
valorPalo = [80 ,70 ,60 , 50]

J1_deno = [ 2 , 10,'a','q']
J1_palo = ['T','C','D','D']

J2_deno= ['a', 8 , 2 ,'a']
J2_palo= ['T','C','D','C']

J3_deno= [ 7 ,'a','k',10 ]
J3_palo= ['T','P','D','D']

# Definir las siguientes Funciones e invocarlas desde el programa principal.

# def puntaje(d,p): #Recibe una carta, es decir, la denominación y el palo. Devuelve el puntaje correspondiente.
# def mayor(a,b,c): #Recibe tres enteros y devuelve el mayor de ellos.

#  Salida esperada para cada Ronda:
#  Jugador 1: 52 Jugador 2: 64 Jugador 3: 57 Levanta el jugador que obtuvo 64 puntos

def puntaje(a,b):
    puntaje=0
    for d in range (len(Deno)):
        if Deno[d]==a:
            puntaje=puntaje+valorDeno[d]

    for p in range (len(palo)):
        if palo[p]==b:
            puntaje=puntaje+valorPalo[p]
    return puntaje

# puntaje(2,"T")

def mayor2(a,b):
    may=0
    if a>b:
        may=a
    else:
        may=b
    return may
#print(mayor2(4,7))

def mayor(a,b,c):
    mayor=mayor2(a,b)
    mayor3=mayor2(mayor,c)
    return mayor3


#print(mayor(a,b,c))
##def mayorde3listas (J1_deno,J1_palo,J2_deno,J2_palo,J3_deno,J3_palo):
##    puntmasgrande=[]
##    for i in range (4):
##        puntaje1= puntaje(J1_deno[i],J1_palo[i]), "obtuvo el jugador 1"
##        puntaje2= puntaje(J2_deno[i],J2_palo[i]), "obtuvo el jugador 2"
##        puntaje3= puntaje(J3_deno[i],J3_palo[i]), "obtuvo el jugador 3"
##        puntajemayor=mayor(puntaje1,puntaje2,puntaje3)
##        puntmasgrande.append(puntajemayor)
##    return puntmasgrande
##
##a=mayorde3listas(J1_deno,J1_palo,J2_deno,J2_palo,J3_deno,J3_palo)
##
##
##for i in range (len(a)):
##    print(a[i], "en la", i+1, "ronda")

for i in range(len(J1_deno)):
    p1=puntaje(J1_deno[i],J1_palo[i])
    print("jugador 1:", p1 )
    p2=puntaje(J2_deno[i],J2_palo[i])
    print("jugador 2:", p2 )
    p3=puntaje(J3_deno[i],J3_palo[i])
    print("jugador 3:", p3 )
    perdio=mayor(p1,p2,p3)
    print("pierde el que obtuvo", perdio)


# hice la funcion que tome me de el puntaje total, de sumar puntaje palo y puntaje valor numerico
# otra funcion que me de el mayor numero de 3
# por ultimo recorro el len de J1PALO que es igual para los 3 casos, es decir, va a recorrer
# 4 veces, una por cada mano.
# directamente, lo que hago es usar las funciones que ya tengo, para imprimir los valores de cada jugador
# usando el "indice" i,  e imprimo jugador y puntaje, luego utilizo la otra funcion para ver cual es mayor
# de los 3.   E imprimo "el mayor" lo obtuvo , **la variable que da como resultado de saber quien es mayor**

























