"""
datos de entrada
chelines autriacos--->ca--->float
pesetas--->ps--->float
dracmas griegos--->dg--->float
francos francese--->ff--->float
datos de salida
equivalente pesetas--->eps--->float
equivalente francos franceses--->eff--->float
equivalentes dolares--->ed--->float
equivalentes liras italianas--->eli--->float
"""
#entrada
ca=float(input(" digite el numero de chelines austriacos: "))
ps=float(input(" digite el numero de pesetas: "))
dg=float(input(" digite el numero de dracmas griegos: "))
ff=float(input(" didigite el numero de francos franceses: "))
#caja negra
eps=(ca*956.871)
eff=(dg/20.110)
