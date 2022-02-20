"""
datos de entrada
venta_1--->v1--->float
venta_2--->v2--->float
venta_3--->v3--->float
sueldo_b--->sb--->float
datos de salida
comision--->c--->float
"""
#entradas
v1=float(input("digita venta 1: "))
v2=float(input("digita venta 2: "))
v3=float(input("digita venta 3: "))
sb=float(input("digita sueldo base: "))
#salida
c=(v1*0.1)+(v2*0.1)+(v3*0.1)
print("comison por ventas:",c)
print("sueldo total", sb+c)