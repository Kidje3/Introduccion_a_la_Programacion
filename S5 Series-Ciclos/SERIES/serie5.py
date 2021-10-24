# S =    0.5     0.277    0.32465.... 0.31825....
n = int(input("Cantidad de terminos..."))
if n<=0:
    print("debe ingresar un numero natural")
else:
    suma = 0
    signo =  1
    for i in range(1,n+1)  :

            suma = suma + i / (i + 1)**i * signo
            signo = signo * (-1)
            print(i,suma)
    print("la serie para", n , "terminos es",suma)