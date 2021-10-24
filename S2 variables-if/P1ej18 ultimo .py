#P1 ej 18
#seg a dias + horas+ min + seg

tiempo=int(input("ingrese el tiempo en segundos"))

d=tiempo//(60*60*24)
resto=tiempo%(60*60*24)
h=resto//(60*60)
resto=resto%(60*60)
m=resto//60
s=resto%60
print("d -",tiempo,"segundos, equivalen a :",d,"dias",h,"horas",m,"minutos", s,"segundos")

