# Ejercicio 2:

##  La biblioteca de la universidad asigna un código a cada libro que posee. El mismo se conforma con las
##  consonantes del título que no estén repetidas y 4 dígitos con la cantidad de páginas, en caso de tener
##  más de 9999 páginas se mostrarán los últimos dígitos.
##  Ejemplo: Título: “eternamente” Cantidad de hojas: 918 Salida: “RM0918”
##  Hacer una función que reciba el título y la cantidad de páginas de un libro y devuelva el código.


# Codigo= consNOrepetidas + cantHojas




#funcion para saber cuantas letras hay en una palabra
def cantletrasencadena(palabra,letra):
    cont=0
    for char in palabra:
        if char in letra:
            cont=cont+1
    return cont

# desprender solo las consonantes en una cadena

def soloCons(titulo):
    codigo=""
    cons="bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    for char in titulo:
        if char in cons:
            codigo=codigo+char
        codigo=codigo.upper()
    return codigo
#print(codigo)

# generar una nueva cadena usando la funcion de contar, para dejar solo las que no se repiten

def noRepiten (codigo):
    codigo2=""
    for letra in codigo:
        if cantletrasencadena(codigo, letra)==1:
            codigo2=codigo2+letra
    return codigo2

def partenumerica(cantHojas):

    if len(cantHojas)<4:
        agregar0=4-len(cantHojas)
        cantHojas=("0"*agregar0) + cantHojas
        return cantHojas

    elif len(cantHojas)>4:
        hojas2=""
        rango=len(cantHojas)-4
        for i in range (rango,len(cantHojas)):
            hojas2=hojas2+ cantHojas[i]
        return hojas2


def generadorCodigo (titulo, cantHojas):
    codigo=soloCons(titulo)
    codigo2=noRepiten (codigo)
    codigo3=partenumerica(cantHojas)
    codfinal=str(codigo2)+str(codigo3)
    return codfinal

titulo="eternamente"
cantHojas="478951561321351"

print(generadorCodigo(titulo,cantHojas))






