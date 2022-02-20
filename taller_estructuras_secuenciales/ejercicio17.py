"""
datos de entrada
sueldo--->s--->float
salidas
dinero ginecologia--->dg--->float
dinero traumatologia---dt--->float
dinero pediatria--->dp--->float
"""
#entrada
s=float(input(" digite el sueldo: "))
#caja negra
dg=(s*0.40)
dt=(s*0.30)
dp=(s*0.30)
#salidas
print("catida de dinero ginecologia: ", dg)
print("catida de dinero traumatologia: ", dt)
print("catida de dinero pediatria: ", dp)