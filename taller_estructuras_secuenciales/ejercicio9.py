"""
datos de entrada
sueldo base--->sb--->float
numero de horas trabjadas--->nh--->int
precio de la hora--->ph--->float
datos de salida
salario neto--->sn--->float
"""
#entradas
sb=float(input(" digite el sueldo base: "))
nh=int(input("digite el nuumero de horas trabajadas: "))
ph=float(input(" digite el precio de la hora: "))
#caja negra
sn=(sb*nh*ph*0.20)
#salidas
print("el salario neto es: ", sn)