def contarPalabra (palabra,cadena):
    pal=""
    cont=0
    for le in cadena.lower():
        if(le>="a" and le<="z"  or le=="ñ" or le=="á" or le == "é" or le == "í" or le =="ó" or le =="ú" or le =="ü") :
            pal=pal+le
            print(pal)
        else:
            if  pal==palabra.lower():
                cont=cont+1
            pal=""
    return cont




frase="La cantidad de arroz: Si llenamos un vaso de agua con arroz, ésto será la medida para dos personas. Por tanto, 1/2 vaso es la medida de una persona. Aparentemente, puede parecer poco pero esto es muy engañoso. El arroz va absorber mucha agua en la cocción y va a triplicar su tamaño. Prueba a hacer esto y verás como nunca te vuelves a pasar con la cantidad de arroz."
palabra="arroz"

cant=contarPalabra(palabra,frase)
print("La palabra", palabra,"Se encuentra", cant, "veces")