"""
datos de entrada
persona_1--->p1--->int
persona_2--->p2--->int
perosna_3--->p3--->int
datos de salida
promedio_edad--->p_edad--->float
"""
#entradas
p1=int(input("digite edad persona 1 : "))
p2=int(input("digite edad persona 2 : "))
p3=int(input("digite edad persona 3 : "))
#caja negra
p_edad=(p1+p2+p3)/3
print("el promedio de edad es: ", p_edad)