# s = 1 + 2 + 3/4 + 4/9 + 5/16 +....

# s = 1 + 2/(1**2) + 3/(2**2) + 4/(3**2) + 5/(4**2) +....
n= int(input("Cant. de terminos"))
s=1
for i in range(1,n)   :

        s = s + (i+1)/( i  ** 2)


print("la serie para",n,"terminos es",s)