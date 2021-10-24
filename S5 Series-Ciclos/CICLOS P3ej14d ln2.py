import math
e=float(input("error admisible..."))
log2=  math.log(2)
print("logaritno natural de 2 =",log2)
# S = 1/1 -1/2 + 1/3 - 1/4 +.....+-1/i
suma = 0
signo =  1
n=0
i=1
while( abs(suma - log2))>= e:
    suma = suma + 1/i  * signo
    i=i+1
    n=n+1
    signo = signo * (-1)
#    print("n:",n,"suma:",suma,"diferencia:",(log2 - suma))
print("necesite", n, "terminos para un error menor a",e)
