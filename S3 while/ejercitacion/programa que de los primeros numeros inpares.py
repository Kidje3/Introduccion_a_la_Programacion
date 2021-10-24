
#hacer un programa que sume los primeros numeros impares hasta n
# n lo indica el usuario


sumadenumeros=int(input("indique la cantidad de numeros que desea sumar"))
cont=0
acumulador=0

while cont<sumadenumeros:
    cont=cont+1
    acumulador=acumulador+cont
    if acumulador%2!=0:
        print(acumulador)






