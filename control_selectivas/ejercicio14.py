"""
Datos de entrada
lectura actual-->lact-->int
lecturaanterior-->lant-->int
Datos de salida
monto a pagar-->mp-->float
"""
#Entrada
lact=int(input("Ingrese la lectura actual: "))
lant=int(input("Ingrese la lectura anterior: "))
#Caja negra
dif=lant-lact
if(dif>=0) and (dif<=100):
    mpag=dif*4600
elif(dif>=101) and (dif<=300):
    mpag=dif*80000
elif(dif>=301) and (dif<=500):
    mpag=dif*100000
elif(dif>=501):
    mpag=dif*120000
#Salida
print("El monto a pagar del suscriptor sera: ", mpag)