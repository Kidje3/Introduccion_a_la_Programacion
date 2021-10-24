a=int(input("Ingrese año"))

if (a%4 == 0  and  a%100 != 0) or ( a%400 == 0 )   :
    print(a,"es bisiesto")
else:
    print(a,"NO es bisiesto")

