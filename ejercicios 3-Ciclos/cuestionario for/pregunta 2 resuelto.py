#f= 1 -  1/8 +  1/81  - 1/1024 + 1 / 15625   = 0.8864331165123457

g= 1- (1/(2**3))  + (1 /(3**4))  - (1/(4**5))  + (1 / (5**6))
print(g)


cantidad = 5
numerador = 1

serie=1

for b in range (1, cantidad ):   #cant   , cant +1    cant - 1
    if b %2 == 0 :
        numerador = -1      #-1  , 0   ,  1
    else:
        numerador = 1

    d= numerador/ b** (b+1)     # (b+1 ) ,  exp ,  (b+b)

    serie = serie + d

print (serie)






