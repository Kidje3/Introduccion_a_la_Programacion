# ej 3 de pdf  hacer un programa que nos indique si una frase dada tiene alguna mayuscula.

frase= input("ingrese una frase")

cont=0
for letra in frase:
    if letra >= "A" and letra <= "Z":

        cont=cont+1

if cont >= 1:
    print ("tiene mayusculas")
else:
    print("no tiene mayusculas")





