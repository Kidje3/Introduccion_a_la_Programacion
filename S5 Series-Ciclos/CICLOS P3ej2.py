m = int(input("Ingrese numero donde quiere empezar"))
n = int(input("Ingrese numero donde quiere terminar."))
# version while
##i = m
##print("version while")
##while i <= n :
##    print( i, end = " ")
##    i = i + 1
##
##i = m
##while i >= n :
##    print( i, end = " ")
##    i = i - 1
##print()



print("version for")
# version for
for i in range(m,n-1,-1)  :
    print( i, end = " ")
for i in range(m,n+1,1) :
    print( i, end = " ")
