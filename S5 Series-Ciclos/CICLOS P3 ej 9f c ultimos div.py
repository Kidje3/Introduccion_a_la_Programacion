
# ej P3-9f)
# ULTIMOS C dividores de n

c=int(input("Ingrese la cantidad de divisores que necesita ver"))
n=int(input("Ingrese el numero del cual quiere saber los divisores"))
print("ULTIMOS",c,"divisores de",n)
k=0
i=n

while(k<c and i>=1):
    if(n%i==0):
        k=k+1
        print (k,"- divisor de ",n,"es ",i)
    i=i-1
if k<c:
    print( "no hay mas divisores")
