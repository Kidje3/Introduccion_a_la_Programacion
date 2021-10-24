#P2ej10 KW
print ("Este programa calcula el precio a pagar en la factura de LUZ")
tarifafija=480
kwlibre=200
pr_excedente=25.50
impuestos=78


kwinicial=float(input("Ingrese KW iniciales"))
kwfinal=float(input("Ingrese KW final"))
kw=kwfinal-kwinicial


if(kw<=200):
    monto=tarifafija+impuestos
else:
    monto=tarifafija+impuestos+pr_excedente*(kw-kwlibre)

print("El precio a pagar es:",monto)