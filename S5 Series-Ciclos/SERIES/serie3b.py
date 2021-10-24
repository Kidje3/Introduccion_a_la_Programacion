# S = 1/1 + 1/3 + 1/5 + 1/7 +.....+1/i

n = int(input("Cantidad de terminos..."))
if n<=0:
    print("debe ingresar un numero natural")
else:
    suma = 0
    for i in range(1,n+1,1)  :  # 1 2 3 4 ... n
        suma = suma + 1/(2*i-1)
        print(i,suma)
    print("la serie para", n , "terminos es",suma)

    # 1 1.333 1.5333