# ejercicio 3 de series

n=int(input("ingrese un valor entero mayor a 0"))


s=1
for i in range (1, n):
    s= s+ (1/(2*i+1))
    print (s)
print( "la serie para", n, "terminos, es ", s)
