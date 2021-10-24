
import random
print("*** 1-piedra *** 2-papel *** 3-tijera ***\n\n")
maq= random.randint(1,3)
ud= 9
while (ud<1 or ud>3):
    ud= int(input( "Elija :\n\n 1-PIEDRA, 2-PAPEL, 3-TIJERA \n\n"))

#OPCION MAQ
if(maq==1):
    opcion_maq="PIEDRA"
if(maq==2):
    opcion_maq="PAPEL"
if(maq==3):
    opcion_maq="TIJERA"



#OPCION UD
if(ud==1):
    opcion_ud="PIEDRA"
if(ud==2):
    opcion_ud="PAPEL"
if(ud==3):
    opcion_ud="TIJERA"



print("Ud. eligio ", ud, opcion_ud, " - y Yo  ", maq, opcion_maq)

if(maq==ud):
    print ("- - - - - - - -")
    print ("< E M P A T E >")
    print ("- - - - - - - -")
else:
    if( (maq==1 and ud==2) or (maq==2 and ud==3) or (maq==3 and ud==1)  ):
        print ("********************")
        print ("* Ud. G A N O  !!! *")
        print ("********************")
    else:
        print ("*** * * * * * * * * * ***")
        print ("* Ud. P E R D I O  !!!  *")
        print ("*** * * * * * * * * * ***")

print("\n\ncontrole ==> 1-PIEDRA, 2-PAPEL, 3-TIJERA")
