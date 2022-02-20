"""
datos de entrada
mujeres--->m--->int
hombres--->h--->int
datos de salida
porcentaje mujeres--->ph--->float
porecentaje hombres--->pm--->float
"""
#entadas
m=int(input("ingrese cantida de mujeres: "))
h=int(input("ingrese cantidad de hombres: "))
#caja negra
total=h+m
ph=(h/total)*100
pm=(m/total)*100
#salidas
print(f"el porcentaje de hombres es: {ph}%")
print(" el porcentaje de mujeres es: "+str(pm)+"%")