#-------------------------------------------------------------------------------
n = int(input("Cantidad de terminos..."))
if n<=0:
    print("debe ingresar un numero natural")
else:
    suma = 0
    for i in range(2,n+1,1)  :
        suma = suma + i / (i - 1) ** 2
    suma = suma + 1
    print("la serie para", n , "terminos es",suma)
#  1 3  3.75 4.1944
