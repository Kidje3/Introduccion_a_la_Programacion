# Realizar un programa que sume los primeros n números
# naturales. (n lo indica el usuario) 1+2+3+4+…+n =


sumadenumeros=int(input("indique la cantidad de numeros que desea sumar"))
cont=0
acumulador=0

while cont<sumadenumeros:
    if acumulador%5==0:
        cont=cont+1
        acumulador=acumulador+cont
        print(acumulador)




