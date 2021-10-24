# Hacer un programa que sume los primeros n naturales múltiplos de 5 y determine la cantidad
# mínima de términos necesarios para superar un valor tope que se solicita previamente al usuario.


#5 + 10 + 15 + ..... > tope

#Ejemplo :

#   si tope = 85 debe informar 6 terminos, porque:

#    s = 5 + 10 + 15 + 20 + 25 + 30 = 105 que es mayor que 85 (con 1 término menos, la suma da 75 que es menor que 85).


tope=int(input("ingrese valor tope"))

tabla5=0
acum=0
i=0
while acum  <tope:
    tabla5=tabla5+5
    acum=acum+tabla5
    i=i+1
print("la cantidad minima de terminos necesarios para superar tope ingresado es: ", i, "terminos")



