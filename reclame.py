from algemene_functies import mijn_functie_2

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[1])
    return uitvoer

def aanbieding_1(smaak, prijs, korting):
    prijs = 4
    nieuwe_prijs = prijs * (1 - korting)
    
    boodschap = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
    
    return boodschap


resultaat = aanbieding_1("aardbei", 4, 0.1)
print(resultaat)

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
    btw_bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return uitvoer

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09

print(inkomsten_totaal(inkomsten, btw))  

def laag_en_hoog(mijn_lijst):
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten_per_dag)

print(resultaat)

def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    totaal = 0
    for element in mijn_lijst:
        totaal += element
    gemiddelde = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."

inkomsten = [220, 430, 125, 160, 205, 90, 345]

print(gemiddelde(inkomsten))
def meervoudig(invoer_lijst):
    {
        10,
        5,
        3,
        2,
        1,
        2,
        9,
     }
    laagste = min(invoer_lijst)
    hoogste = max(invoer_lijst)
    
    return [laagste, hoogste]

lijst = [10,5,3,2,1,2,9]
resultaat = meervoudig(lijst)

print(resultaat)