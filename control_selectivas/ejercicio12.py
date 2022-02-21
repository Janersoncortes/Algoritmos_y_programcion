"""
Datos de entrada
Cantidad_COP-->cCOP-->int
Datos de salida
Cantidad_billete_monedas-->cbm-->float
"""
#Entrada
cCOP=float(input("Ingrese la cantidad de COP (entera): "))
#Caja negra
COP= list()
for i in (100000,50000,20000,10000,5000,2000,1000,500,200,100,50):
    if cCOP >= i:
        COP.append(int(cCOP/i)*i)
        cCOP=cCOP-int(cCOP/i)*i
    else: 
        cCOP=cCOP
cbm=str(COP)[1:-1]
#Salida
print("El desgloce de la cantidad de dinero es: ", cbm)