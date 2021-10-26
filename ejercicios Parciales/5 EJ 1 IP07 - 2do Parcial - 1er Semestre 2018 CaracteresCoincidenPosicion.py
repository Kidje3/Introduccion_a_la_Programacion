# ejercicio1

##  Escribir una función que reciba dos cadenas, y que devuelva una cadena conteniendo los
##  caracteres que coinciden por posición. Por ejemplo, si las dos cadenas de entrada son:
##
##    “tinteres​ante manera​”
##    “tpara es​conder pala​bras”
##
##  la función deberá retornar la cadena “esa”​ .


cadena1="tinteresante manera"
cadena2="tpara esconder palabras"



def caracteresCoinciden (cadena1, cadena2):
    nueva=""
    for i in range (len(cadena1)):
        if cadena1[i]==cadena2[i]:
            nueva=nueva+cadena1[i]
    return nueva

print(caracteresCoinciden(cadena1,cadena2))










