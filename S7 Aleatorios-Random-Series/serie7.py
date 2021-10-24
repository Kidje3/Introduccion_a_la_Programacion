##s= 1/2 + 1 + 3/4 + 1 + 5/2 + 3 + 7/4 + 2
##s= 1/2 + 2/2 +3/4 + 4/4 + 5/2  + 6/2 + 7/4 + 8/4  + 9/2 + 10/2

n= int(input("Cant. de terminos"))
s=0
for i in range(1,n+1)   :
    if i%4 == 1 or i%4 == 2   :
        den = 2
    else:
        den = 4

    s = s + i / den

print("la serie para",n,"terminos es",s)
