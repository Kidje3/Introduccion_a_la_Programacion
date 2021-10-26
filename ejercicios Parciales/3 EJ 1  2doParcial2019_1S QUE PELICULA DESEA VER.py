# ejercicio1

##  El cine del barrio decide sistematizar la venta de entradas, cuentan con 6 salas que emiten una función
##  diaria y cada sala tiene una capacidad distinta. Los compradores eligen una película y avisan cuantas
##  entradas desea, el sistema avisa en que sala tienen que ingresar o si ya no hay disponibilidad.
##  En caso de haber disponibilidad se deberá descontarla de la lista de capacidad disponible de esa sala.

Salas                     = [ 1,         2,       3,     4,        5,            6   ]
Peliculas                 = [ "xmen", "titanic", "saw", "rio", "taxi driver", "avatar"]
CapacidadDisponiblePorSala= [ 80,        3,      60,    75 ,     40,            90  ]





a=input("Que pelicula desea ver")

peliculaPedida=a.lower()
cuantasEntradasQuiere= int(input("Cuantas entradas desea comprar"))
for i in range (len(Peliculas)):
    if Peliculas[i]==peliculaPedida:
        print ("la pelicula:", Peliculas[i], "esta en Sala", Salas[i])
        if (CapacidadDisponiblePorSala[i]-cuantasEntradasQuiere)>=0:
            print("quedan:", CapacidadDisponiblePorSala[i], "entradas" )
            CapacidadDisponiblePorSala[i]=CapacidadDisponiblePorSala[i]- cuantasEntradasQuiere
            print("si compra, la nueva disponibilidad es:", CapacidadDisponiblePorSala[i], "entradas")
        else:
            print("No hay disponibilidad")














