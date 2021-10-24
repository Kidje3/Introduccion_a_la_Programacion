# S = 1/1 -1/2 + 1/3 - 1/4 +.....+-1/i

n = int(input("Cantidad de terminos..."))
if n<=0:
    print("debe ingresar un numero natural")
else:
    suma = 0
    signo =  1
    for i in range(1,n+1,1)  :

            suma = suma + 1/i  * signo
            signo = signo * (-1)


    print("la serie para", n , "terminos es",suma)