def mijn_functie_1(a):
    return a * a

print(mijn_functie_1(2))  
print(mijn_functie_1(4))   
print(mijn_functie_1(10))  
print(mijn_functie_1(12))  

def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst

[(12, 3)] , [(12, 2)] , [(10, 5)] , [(100, 20)]

print(mijn_functie_2(12, 3))
print(mijn_functie_2(12, 2))
print(mijn_functie_2(10, 5))
print(mijn_functie_2(100, 20))