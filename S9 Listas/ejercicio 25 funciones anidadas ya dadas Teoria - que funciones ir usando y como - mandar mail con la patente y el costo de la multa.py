##Ejercicio 25
##  Hacer una función que automatice el control vehicular en rutas nacionales. Hacer el control
##  para la Ruta Nacional 8 durante *un día completo*, se debe controlar que los automóviles no
##  **superen 100 km/h** y en caso de hacerlo se les enviará una multa a sus hogares, si es reincidente
##  la multa se duplica. Para ello cuenta con las siguientes funciones.

##  - darPatentes(ruta): Dada una ruta nacional devuelve una lista con todas las patentes de los
##  autos que pasaron en el día.

##  - controlVelocidad(patente): Recibe un número de patente y devuelve la velocidad a la que
##  cruzó el radar dicho automóvil.

##  - reincidente(patente): Devuelve True en caso de que la patente ya tenga multas por exceso
##  de velocidad.

##  - costoActual(): No recibe parámetros y devuelve el costo por superar la velocidad permitida.

##  - enviarMulta(patente, costo): Manda una multa al domicilio del propietario del automóvil
##  con el costo.

def controlVehicular(ruta):
    patentes=darPatentes(ruta)
    costo=costoActual()
    for patente in patentes:
        if controlVelocidad(patente)>100:
            if reincidente(patente):
                costoMulta=costo*2
            else:
                costoMulta=costo
            enviarMulta(patente,costoMulta)

# las funciones suelen estar anidadas, ver con cual comenzar, para ir sacando datos.
# ej va de lo general a lo particular.