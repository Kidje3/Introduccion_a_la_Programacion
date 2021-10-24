#  s= 1/1 + 1/3 + 1/6 + 1/10 + 1/15 +....

n= int(input("Cant. de terminos"))
den=0
s=0
for i in range(1,n+1)   :
        den = den + i
        s = s + 1/den


print("la serie para",n,"terminos es",s)
