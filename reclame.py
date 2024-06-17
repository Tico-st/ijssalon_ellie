from algemene_functies import mijn_functie_2

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

def aanbieding_1(smaak, prijs, korting):
    prijs = 4
    nieuwe_prijs = prijs * (1 - korting)
    
    boodschap = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
    
    return boodschap


resultaat = aanbieding_1("aardbei", 4, 0.1)
print(resultaat)

def inkomsten_totaal(inkomsten):
    {
        "Maandag" : 220,
        "Dinsdag" : 430,
        "Woensdag" : 125,
        "Donderdag" : 160,
        "Vrijdag" : 205,
        "Zaterdag" : 90,
        "Zondag" : 345,
    }
def tel_op(Maandag,Dinsdag,Woensdag,Donderdag,Vrijdag,Zaterdag,Zondag):
    return Maandag + Dinsdag + Woensdag + Donderdag + Vrijdag + Zaterdag + Zondag
    
totaal = tel_op (220, 430, 125, 160, 205, 90, 345)
print(totaal)

btw = 0.09
bedrag = totaal * btw

print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    {
        220,
        430,
        125,
        160,
        205,
        90,
        345,
    }
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    
    return [laagste, hoogste]

inkomsten = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten)

print(resultaat)

def gemiddelde(mijn_lijst):
    {
        "Maandag" : 220,
        "Dinsdag" : 430,
        "Woensdag" : 125,
        "Donderdag" : 160,
        "Vrijdag" : 205,
        "Zaterdag" : 90,
        "Zondag" : 345,
    }
def tel_op(Maandag,Dinsdag,Woensdag,Donderdag,Vrijdag,Zaterdag,Zondag):
    return Maandag + Dinsdag + Woensdag + Donderdag + Vrijdag + Zaterdag + Zondag
    
totaal = tel_op (220, 430, 125, 160, 205, 90, 345)

bedrag = (totaal / 7)

print(f"De gemiddelde inkomsten deze week zijn {bedrag} euro.")

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

