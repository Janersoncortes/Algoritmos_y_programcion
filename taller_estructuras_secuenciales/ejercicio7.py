"""
datos de entrada
metros--->m--->int
salidas
pulgadas--->p--->float
pies--->p_e--->float
"""
#entrada
m=int(input("digite cantida de metros: "))
#caja negra
p=(m*39.27)
p_e=(p/12)
#salidas
print("la conversion de metros a pulgadas es: ", p)
print(" la conversion de metros a pies es: ", p_e )
