"""
datos de entrasda
billetes de 50000--->b50k--->int
billetes de 20000--->b20k--->int
billetes de 10000--->b10k--->int
billetes de 5000--->b5k--->int
billetes de 2000--->b2k--->int
billetes de 1000--->b1k--->int
billetes de 500--->b5p--->int
datos de salida
cantidad billetes de 50000--->cb50k--->int
cantidad billetes de 20000--->cb20k--->int
cantidad billetes de 10000--->cb10k--->int
cantidad billetes de 5000--->cb5k--->int
cantidad billetes de 2000--->cb2k--->int
cantidad billetes de 1000--->cb1k--->int
cantidad billetes de 500--->cb5p--->int
total--->tl--->int
"""
#entrada
b50k=int(input(" digite el numero de billetes de 50000: "))
b20k=int(input(" digite el numero de billetes de 20000: "))
b10k=int(input(" digite el numero de billetes de 10000: "))
b5k=int(input(" digite el numero de billetes de 5000: "))
b2k=int(input(" digite el numero de billetes de 2000: "))
b1k=int(input(" digite el numero de billetes de 1000: "))
b5p=int(input(" digite el numero de billetes de 500: "))
#caja negra
cb50k=(b50k*50000)
cb20k=(b20k*20000)
cb10k=(b10k*10000)
cb5k=(b5k*5000)
cb2k=(b2k*2000)
cb1k=(b1k*1000)
cb5p=(b5p*500)
tl=(cb50k+cb20k+cb10k+cb5k+cb2k+cb1k+cb5p)
#salida
print("la cantidad de billetes de 50000 es: ", cb50k)
print("la cantidad de billetes de 20000 es: ", cb20k)
print("la cantidad de billetes de 10000 es: ", cb10k)
print("la cantidad de billetes de 5000 es: ", cb5k)
print("la cantidad de billetes de 2000 es: ", cb2k)
print("la cantidad de billetes de 1000 es: " , cb1k)
print("la cantidad de billetes de 500 es: ", cb5p)
print("la cantidad de plata es: ", tl)

