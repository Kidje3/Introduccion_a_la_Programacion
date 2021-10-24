# ejercicio 10

# Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en
# pantalla el producto (es decir, la multiplicación) de los numeros entre 1 y n


#  n , muestre:  nx1   nx2   nx3   nx4  nx5  ----> n*n



n=int (input("ingrese un numero positivo"))



for i in range (1,n+1):
    multiplicacion=n*i
    print(multiplicacion)

