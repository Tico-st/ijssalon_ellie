def presenteer(inkomsten, totaal):
    for key, value in inkomsten.items():
        print(f"{key} : {value} euro")
    print("=" * 26)
    print(f"totaal : {totaal} euro"
