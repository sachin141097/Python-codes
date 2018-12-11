maths = {1,2,3,5,7,9}
physics = {2,4,6,9}
chemistry = {1,3,5,9}

MP = maths & physics
CM = maths & chemistry
PC = physics & chemistry
PCM = maths & chemistry & physics

print("Physics and chemistry :",PC)
print("Maths and chemistry :",CM)
print("Physics and maths :",MP)
print("All subjects :",PCM)

M = maths - MP - CM
P = physics - MP - PC
C = chemistry - CM - PC

print("Only Maths : ",M)
print("Only Physics : ",P)
print("Only Chemistry : ",C)
