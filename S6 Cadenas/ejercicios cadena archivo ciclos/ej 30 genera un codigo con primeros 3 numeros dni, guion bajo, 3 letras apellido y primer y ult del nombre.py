# en este ejercicio lo que nos pide es que hagamos un legajo con los primeros 3 numeros del dni, luego un guion bajo
#  luego las primeras 3 letras del apellido, y por ultimo , la primer y ultima letra del nombre.

nombre= input("ingrese su nombre")
apellido= input  ("ingrese su apellido")
dni= input("ingrese su DNI")


nueva=""

# 1° buscamos los primeros 3 numeros del dni
for letra in dni:
    if len(nueva) != 3:     # lo que hace es, si len de nueva es distinto de 3, le agrega la letra a nueva.  Arranca de nueva vacia.
        nueva=nueva + letra

# 2° agrego un guion bajo
nueva= nueva + "_"      # le agrego un guion bajo

# 3°  agrego las 3 primeras letras del apellido
for letra in apellido:
    if len(nueva) < 7:    # en ese caso, va a contar 3 caracteres mas el _ , y va a completar con las 3 primeras letras de apellido.
        nueva=nueva + letra

# 4° ahora le tengo que agregar el primer y ultimo del nombre
cant=1
for letra in nombre:
    if cant ==1:    # inicializo cant en 1 porque necesito que adjunte el primer caracter del nombre
        nueva=nueva + letra
    if cant == len (nombre):    # decir len(nombre) es lo mismo que decir el ultimo caracter del nombre, entonces le agrega el ultimo.
        nueva = nueva + letra
    cant= cant + 1
print(nueva)


