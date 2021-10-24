# S= 1 -  1/2 + 1/3 - 1/4 + ....

n= int(input("Cant. de terminos"))

s=0
for i in range(1,n+1)   :

        s = s + 1/i * (-1) ** (i+1)
        print (s)

print("la serie para",n,"terminos es",s)
