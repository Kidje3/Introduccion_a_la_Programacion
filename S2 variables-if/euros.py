monto=int(input("Dinero a desglosar"))

b500= monto//500
resto= monto%500
b200= resto//200
resto=resto%200
b100= resto//100
resto=resto%100
b50=  resto//50
resto=resto%50
b20=resto//20
resto=resto%20
b10=  resto//10
resto=resto%10
b5=   resto//5
resto=resto%5
m2=   resto//2
resto=resto%2
m1=resto//1

print("el dinero a desglosar es:",monto)
print(b500, "billetes de 500 euros.")
print(b200, "billetes de 200 euros.")
print(b100, "billetes de 100 euros.")
print(b50, "billetes de 50 euros.")
print(b20, "billetes de 20 euros.")
print(b10, "billetes de 10 euros.")
print(b5, "billetes de 5 euros.")
print(m2, "monedas de 2 euros.")
print(m1, "monedas de 1 euro.")