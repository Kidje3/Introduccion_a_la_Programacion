

#función ESTA el entero en una lista

def esta(entero,lista):
    for elem in lista:
        if elem == entero:
            return True
    return False


lista=[3,4,6,8,7,55,63,12,32]
b=55


print(esta(b,lista))

