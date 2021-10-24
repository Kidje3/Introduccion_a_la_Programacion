a=int(input("Ingrese primer valor"))
b=int(input("Ingrese segundo valor"))
c=int(input("Ingrese tercer valor"))
print ("inicio", a,b,c)

if(a>b):
    aux=a
    a=b
    b=aux
if(a>c):
    aux=a
    a=c
    c=aux
if(b>c):
    aux=b
    b=c
    c=aux

print("ordenados",a,b,c)
