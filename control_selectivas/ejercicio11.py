"""
datos de entrada
deporte--->d--->str
"""
#entrada
from tkinter.filedialog import SaveFileDialog

t=float(input("digite la temperatura: "))
#caja negra
deporte=""
if(t>85):
    deporte="Natacion"
elif(t>70 and t<=85):
    deporte="Tenis"  
elif(t>32 and t<=70):
    deporte="Golf"
elif(t>10 and t<=32):
    deporte="Esqui"
elif(t>=0 and t<=10):
    deporte="Marcha" 
else:
    deporte="no se encuentra el rango"
#datos de salida
print("el deporte es: "+deporte)           