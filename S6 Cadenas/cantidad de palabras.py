# cantidad de palabras de una frase
# se supone la frase bien escrita (sin espacios sobrantes)

frase=input("Ingresar frase")

if(len(frase)==0):
    print("la frase no existe, no tiene palabras")
else:
    cantPal=0
    for letra in frase:
        if letra==" " :
            cantPal=cantPal+1
    print("la frase :",frase,", tiene:",cantPal+1,"palabras.")
