"""
Datos de entrada
inversion--->i--->int
tasa de interes--->it--->int
Datos de salida
intereses--->itr--->float
"""
#entrada
i=int(input(" ingrese la catidad invertida: "))
it=int(input(" ingrese la tasa de interes: "))
#caja negra
cit=i*it/100
print("interes: $",cit)
if (cit>100000):
    "los intereses superan 100000"
else:
    "los interese no superan 100000"
    print("la cantidad total con interese es ",cit+i)