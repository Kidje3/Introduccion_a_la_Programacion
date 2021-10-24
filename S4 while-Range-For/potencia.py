# a elevado a b ( a**b)

base=int(input("Ingrese base"))
exponente=int(input("Ingrese exponente"))

potencia=1
for i  in range(1,exponente+1,1):
    potencia=potencia*base

print(base,"elevado a la",exponente,"es =", potencia )
