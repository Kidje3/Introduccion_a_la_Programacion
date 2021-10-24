#ORDENAR 2 VALORES

a=int(input("ingrese primer numero"))
b=int(input("ingrese segundo numero"))
print("ingresados",a,b)

if(a>b):
    aux=a
    a=b
    b=aux

print("ordenados ",a,b)
