import random
import math

# generálj 5 véletlen számot [10, 15) között
def veleltlen():
    i:int=0
    list=[] #listában csak azonos típusú adatok legyenek
    while i<=5:
        szam:int= random.random()*(36-10)+10
        list.append(szam) # lista végéhez fűzöm az aktuális elemet
        # list[i]=szam #java csinálja, python nem
        i+=1
    return list

listam=veleltlen()

# írjuk ki egymás alá a lista elemeti
def lista_kiir1(lista):
    for i in range(0, len(lista), 1):
        print(f"A lista {i}. eleme {lista[i]}")

lista_kiir1(listam)

def lista_kiir2(lista):
    i:int=0
    while i<=len(lista):
        print(f"A lista {i}. eleme {lista[i]}")
        i+=1

lista_kiir2(listam)