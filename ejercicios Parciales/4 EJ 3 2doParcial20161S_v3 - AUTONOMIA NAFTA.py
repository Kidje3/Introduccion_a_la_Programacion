# ejercicio 3

##  Una empresa automotriz te contrata para programar el sistema que indica ***la autonomía de un nuevo modelo*** de
##  automóvil.El sistema debe estar constantemente verificando el ritmo de consumo para obtener la autonomía, y si
##  es menor de 50 Km alertar al conductor. Cada 60 segundos debe verificar cuánto combustible hay en el tanque.

##  El sistema provee las siguientes funciones:

## - relojArranque() retorna los segundos transcurridos desde que el auto se puso en marcha.

## - combustibleTanque() retorna el volumen de combustible en el tanque en litros.

## - velocidadAuto() retorna la velocidad a la que viaja el auto en Km por hora.

## - consumoPorVelocidad(velocidad) dada la velocidad retorna el consumo en litros por Km.

## - autonomiaAuto(consumo,combustible) para el ritmo de consumo y el combustible que le queda retorna la
##  distancia que puede recorrer en Km.

## - alertarConductor() envía un alerta cuando le quedan menos de 50 Km.


while True:
    if relojArranque()%60==0:
        combustibleEnTanque  =combustibleTanque()   #nos indica cuanto combustible queda en el tanque
        velocidadxKm         =velocidadAuto()       #nos dice a que velocidad va el auto
        consumoEnLtrs        =consumoPorVelocidad(velocidadxKm)    # segun la velocidad, nos indica consumo de lts.
        if autonomiaAuto(consumoEnLtrs,combustibleEnTanque) < 50:
            alertarConductor()







