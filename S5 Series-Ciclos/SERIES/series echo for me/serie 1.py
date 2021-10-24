# s= 1 + 1/2 + 1/3 + 1/4 + 1/5....

n=int(input("ingrese un valor entero mayor a 0"))


s=0
for i in range (1, n+1):
    s= s+ 1/i
    print (s)
print( "la serie para", n, "terminos, es ", s)



