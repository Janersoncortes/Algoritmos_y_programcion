"""
Datos de entrada
edad--->ed--->int
nivel de hemoglobina--->hm--->int
"""
ed=int(input("digite la edad: "))
hm=int(input("digite el nivel de hemoglobina: "))
anemia=""
if (ed>=0 and ed<1) and (hm>=13 and hm<=26):
    anemia="no tiene anemnia"
elif(ed>=1 and ed<=6) and (hm>10 and hm<=18):    
    anemia="no tiene anemnia"
elif(ed>=6 and ed<=12) and (hm>11 and hm<=15):    
    anemia="no tiene anemnia"
elif(ed>=1 and ed<=5) and (hm>11.5 and hm<=15):    
    anemia="no tiene anemnia"    
elif(ed>=5 and ed<=10) and (hm>12.6 and hm<=15.5):    
    anemia="no tiene anemnia"    
elif(ed>=10 and ed<15) and (hm>13 and hm<=15.5):    
    anemia="no tiene anemnia"    