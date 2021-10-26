# Ejercicio 4

##  Un local de venta de golosinas quiere automatizar la generación del pedido de mercadería que
##  realiza semanalmente a su proveedor mayorista. Sólo se debe incluir en el pedido a los productos
##  que tengan un stock menor a 100 unidades. Si el stock es menor a 50 unidades, se debe solicitar
##  el doble de la cantidad vendida en la última semana. Caso contrario, se pedirá la misma cantidad
##  que se vendió.

##  Armar un programa que automatice el pedido al proveedor, utilizando las siguientes funciones ya
##  disponibles:

##  - Productos()​: Retorna una lista que contiene todos los códigos de producto que vende el local.

##  - StockActual(prod)​: Recibe un código de producto, y retorna el stock actual de unidades.

##  - VentaSemanal(prod)​: Recibe un código de producto, y retorna la cantidad vendida en la última
##  semana.

##  - GenerarPedido(prod, cant)​: Recibe un código de producto y una cantidad, y genera el pedido
##  al proveedor para ese producto

def pedidoMercaderia():
    listaprod=productos()   #trae los codigos de producto
    for prod in listaprod:
        stock=StockActual(prod)  # tira el sock actual de un producto
        vtasemanal=(prod)   #tira cuanto se vendio en la ultima semana.​
        if stock < 50:
            cant=vtasemanal*2
            pedido=GenerarPedido(prod, cant)
            print(pedido)
        if stock <100:
            cant=vtasemanal
            pedido=GenerarPedido(prod,cant)
            print(pedido)

pedidoMercaderia()



