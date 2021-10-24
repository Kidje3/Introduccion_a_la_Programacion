#  ejercicio 27     Escribir un programa que pida al usuario una cadena e indique si esta posee un diptongo (dos vocales unidas).


cadena=input("ingrese una palabra para saber si posee diptongo")

vocal= "aeiou"

cont= 0




for char in cadena:
    if char in vocal:
        cont=cont + 1
        if cont==2:
            print("es diptongo")
        else:
            cont=1
            print("no es diptongo")


