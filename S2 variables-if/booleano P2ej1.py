# Rx   P2ej1 booleano

a = int(input("Ingrese un numero entero"))
b = int(input("Ingrese un numero entero"))
c = int(input("Ingrese un numero entero"))
print("Usted ingreso los valores:", a, b, c)
print(a, "es mayor que", b, a>b)
print(a, "y", b, "son iguales", a==b)
print(a, "es el mayor de todos", a>b and a>c)
print(b, "es el menor de todos", b<a and b<c)
print(a, "es mayor que alguno de los otros dos", a>b or a>c)
print(a, "es menor o igual que alguno de los otros dos", a<=b or a<=c)
print("Los tres numeros son iguales", a==b and b==c)
print("Los tres numeros son distintos", a!=b and a!=c and b!=c)
print(a, "es par", a%2==0)
print("alguno es par", a%2==0 or b%2==0 or c%2==0)
print("ninguno es par", a%2==1 and b%2==1 and c%2==1)
print("todos son pares", a%2==0 and b%2==0 and c%2==0)
print(a, "es multiplo de 3", a%3==0)
print(a, "es multiplo de 3 y de 5", a%3==0 and a%5==0)
print(a, "es multiplo de 3 y par", a%6==0)
print(a, "-", b, "da un numero positivo", a>b)
print(a, "-", b, "da un numero par positivo", a>b and (a%2==b%2))
