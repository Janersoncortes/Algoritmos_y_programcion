"""
datos de entrada
lado_a--->a--->float
lado_b--->b--->float
lado_c--->c--->float
datos de salida
semiperimetro--->s--->float
area--->ar--->float
"""
#entrada
a=float(input("digite el valo del lado a: "))
b=float(input("digite el valor del lado b: "))
c=float(input("digite el valor del lado c: "))
#caja negra
s=(a+b+c)/2
ar=pow(s)*pow((s-a))*pow((s-b))*pow((s-c))
#salidas
print("el valor del semiperimetro es: ", s)
print( "el area es: ", ar)