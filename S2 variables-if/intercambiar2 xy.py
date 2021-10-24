# Intercambiar x y  (sin auxiliar)

x=int(input("Ingrese un numero entero"))
y=int(input("Ingrese otro mnumero entero"))

print("Inicial",     x,y)

x=x+y
y=x-y
x=x-y

print("Final  ",     x,y)
